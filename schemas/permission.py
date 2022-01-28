def permissionsEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "username":item["username"],
        "read":permissionEntity(item["read"]),
        "write":permissionEntity(item["write"]),
        "owner":permissionEntity(item["owner"])
    }


def permissionEntity(entity) -> list:
    return [item for item in entity]