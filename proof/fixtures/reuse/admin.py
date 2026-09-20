def set_collection_hold(service, key, enabled):
    return service.hold(key) if enabled else service.release(key)
