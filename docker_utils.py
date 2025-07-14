from python_on_whales import docker

def get_unhealthy_containers():
    print("all containers:", [c.name for c in docker.ps(all=True)])
    unhealthy_containers = [
        c for c in docker.ps(all=True)
        
        if c.state.health and c.state.health.status == "unhealthy"
    ]
    print(f"Unhealthy containers found: {[c.name for c in unhealthy_containers]}")
    return unhealthy_containers

def restart_container(container):
    docker.restart(container)
    return container.name
