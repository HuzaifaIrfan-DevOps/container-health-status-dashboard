from python_on_whales import docker
import time

CHECK_INTERVAL = 30  # seconds

def check_and_restart():
    containers = docker.ps(all=True)
    print(containers)
    for container in containers:
        health_status = container.state.health.status if container.state.health else None
        if health_status == "unhealthy":
            print(f"🔁 Restarting unhealthy container: {container.name} ({container.id[:12]})")
            docker.restart(container)

if __name__ == "__main__":
    print("🐍🐳 Watchdog using python-on-whales started...")
    while True:
        check_and_restart()
        time.sleep(CHECK_INTERVAL)
