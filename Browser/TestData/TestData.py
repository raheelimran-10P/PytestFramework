class TestData:
    TITLE = "EarthOptics"
    GEOPHEX_TITLE = "GeophexMock"
    IDSGPR_TITLE = "IDSGPRMock"
    MLMODEL_TITLE = "MLModelDevice"
    NUMBER_OF_DEVICE = 1
    DATA_TRANSMISSION_INTERVAL_SECONDS = 2
    DATA_TRANSMISSION_DURATION_SECONDS = 120
    TOPIC_FILTER = "CAN_BUS_PUB"
    TOPIC_NAME = "CAN_BUS_SUB"
    MESSAGE_PAYLOAD_01 = "{\"DataStorageReq\": 0, \"SensorInUseFlag\": 0, \"CompactionThresholdTrgt\": 2241}"
    MESSAGE_PAYLOAD_02 = "{\"DataStorageReq\": 0, \"SensorInUseFlag\": 1, \"CompactionThresholdTrgt\": 2241}"
    MESSAGE_PAYLOAD_03 = "{\"DataStorageReq\": 1, \"SensorInUseFlag\": 0, \"CompactionThresholdTrgt\": 2241}"
    MESSAGE_PAYLOAD_04 = "{\"DataStorageReq\": 1, \"SensorInUseFlag\": 1, \"CompactionThresholdTrgt\": 2241}"
