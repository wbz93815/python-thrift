namespace py RTB

struct ScanData {
    1: required string macAddress,  // 设备mac地址
    2: required string rssi,        // 设备信号强度
}

struct Request {
    1: required list<ScanData> allScanData, // 探针数据
    2: required i32 deviceId, // 设备ID
}

exception RequestException {
    1: required i32 code,
    2: optional string message,
}

service RtbService {
    // 通过设备ID、探针数据，获取RTB数据
    string getRtbByDeviceIdAndScanData(1: Request request) throws (1:RequestException requestException);
}