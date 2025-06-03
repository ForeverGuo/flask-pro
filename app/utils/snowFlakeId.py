import time
import threading

class SnowflakeIDGenerator:
    """
    雪花算法 ID 生成器。

    一个 64 位的 ID 结构：
    0 (1 bit) | timestamp (41 bits) | datacenter ID (5 bits) | worker ID (5 bits) | sequence (12 bits)
    """

    # 位数常量
    __TIMESTAMP_BITS = 41
    __DATACENTER_BITS = 5
    __WORKER_BITS = 5
    __SEQUENCE_BITS = 12

    # 各部分最大值
    __MAX_DATACENTER_ID = (1 << __DATACENTER_BITS) - 1 # 31
    __MAX_WORKER_ID = (1 << __WORKER_BITS) - 1         # 31
    __MAX_SEQUENCE = (1 << __SEQUENCE_BITS) - 1         # 4095

    # 移位量
    __WORKER_ID_SHIFT = __SEQUENCE_BITS
    __DATACENTER_ID_SHIFT = __SEQUENCE_BITS + __WORKER_BITS
    __TIMESTAMP_SHIFT = __SEQUENCE_BITS + __WORKER_BITS + __DATACENTER_BITS

    # 默认纪元时间 (Epoch)：例如 2020-01-01 00:00:00 UTC 的毫秒时间戳
    # 这是 ID 时间戳的起始点，选择一个比你的应用上线时间更早的时间。
    DEFAULT_EPOCH = 1577836800000

    def __init__(self, datacenter_id: int, worker_id: int, epoch: int = DEFAULT_EPOCH):
        """
        初始化雪花 ID 生成器。

        Args:
            datacenter_id (int): 数据中心 ID (0-31)。
            worker_id (int): 工作节点 ID (0-31)，在同一个数据中心内唯一。
            epoch (int): 纪元时间戳，毫秒单位。
        """
        if not (0 <= datacenter_id <= self.__MAX_DATACENTER_ID):
            raise ValueError(f"Datacenter ID must be between 0 and {self.__MAX_DATACENTER_ID}")
        if not (0 <= worker_id <= self.__MAX_WORKER_ID):
            raise ValueError(f"Worker ID must be between 0 and {self.__MAX_WORKER_ID}")
        if epoch >= self._get_current_timestamp_ms():
            raise ValueError("Epoch time must be in the past.")

        self.datacenter_id = datacenter_id
        self.worker_id = worker_id
        self.epoch = epoch

        self._last_timestamp_ms = -1  # 上次生成 ID 的时间戳 (毫秒)
        self._sequence = 0            # 同一毫秒内的序列号

        self._lock = threading.Lock() # 线程锁，保证并发安全

    def _get_current_timestamp_ms(self) -> int:
        """获取当前毫秒级时间戳"""
        return int(time.time() * 1000)

    def _wait_for_next_ms(self, last_timestamp: int) -> int:
        """
        当序列号用尽时，等待到下一毫秒。
        当检测到时钟回拨时，也会等待时钟追上。
        """
        timestamp = self._get_current_timestamp_ms()
        while timestamp <= last_timestamp:
            time.sleep(0.001) # 等待 1 毫秒
            timestamp = self._get_current_timestamp_ms()
        return timestamp

    def generate_id(self) -> int:
        """
        生成一个唯一的雪花 ID。
        """
        with self._lock:
            current_timestamp = self._get_current_timestamp_ms()

            # 处理时钟回拨：
            # 如果当前时间小于上次生成 ID 的时间，说明时钟回拨了。
            # 严格模式下应该报错，或者等待时钟追上。
            if current_timestamp < self._last_timestamp_ms:
                # 警告或报错，这里选择报错，因为时钟回拨会导致重复ID
                raise RuntimeError(
                    f"Clock moved backwards. Refusing to generate ID for "
                    f"{self._last_timestamp_ms - current_timestamp} ms."
                )

            # 如果在同一毫秒内：
            if current_timestamp == self._last_timestamp_ms:
                self._sequence = (self._sequence + 1) & self.__MAX_SEQUENCE
                # 序列号已用尽，等待下一毫秒
                if self._sequence == 0:
                    current_timestamp = self._wait_for_next_ms(self._last_timestamp_ms)
            # 如果是新的毫秒：
            else:
                self._sequence = 0

            self._last_timestamp_ms = current_timestamp

            # 组合所有部分以生成 ID
            # 时间戳部分需要减去纪元时间
            id = (
                ((current_timestamp - self.epoch) << self.__TIMESTAMP_SHIFT) |
                (self.datacenter_id << self.__DATACENTER_ID_SHIFT) |
                (self.worker_id << self.__WORKER_ID_SHIFT) |
                self._sequence
            )
            return id
        
def get_unique_id(a=1, b=1):
    snowflake = SnowflakeIDGenerator(a,b)
    return snowflake.generate_id()