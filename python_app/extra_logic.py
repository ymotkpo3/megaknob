import app_builder


def mergeApps(oldApps, newApps):

    old_ids = []
    new_ids = []

    for app in oldApps:
        old_ids.append(app.topProcessPID)

    for app in newApps:
        new_ids.append(app.topProcessPID)
        
    result = []

    # Mantener orden anterior
    for app in oldApps:
        if app.topProcessPID in new_ids:
            result.append(app)

    # Agregar nuevas al final
    for app in newApps:
        if app.topProcessPID not in old_ids:
            result.append(app)

    return result

