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


def replacelist(element1,element2,listval) -> list:
        return list(map(lambda x: x.replace(element1, element2), listval))