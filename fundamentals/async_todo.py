import asyncio
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TaskStore:
    def __init__(self) -> None:
        self.tasks: list[Task] = []
        self._next_id: int = 1

    def add(self, title: str) -> Task:
        task = Task(id=self._next_id, title=title)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Optional[Task]:
        return next((t for t in self.tasks if t.id == task_id), None)

    def complete(self, task_id: int) -> bool:
        task = self.get(task_id)
        if task is None:
            return False
        task.done = True
        return True


async def slow_add(store: TaskStore, title: str) -> Task:
    await asyncio.sleep(0.5)
    return store.add(title)


async def main() -> None:
    store = TaskStore()

    # run three slow_adds concurrently not sequentially
    results = await asyncio.gather(
        slow_add(store, "buy groceries"),
        slow_add(store, "train legs"),
        slow_add(store, "read LiteLLM source"),
    )

    for task in results:
        print(f"added: {task.id} - {task.title}")

    store.complete(1)
    task = store.get(1)
    if task is not None:
        print(f"task 1 done: {task}")


asyncio.run(main())
