__version__ = "0.0.0"

from datetime import datetime
from typing import List

import typer

from joint_teapot.teapot import Teapot

app = typer.Typer(add_completion=False)
teapot = Teapot()


@app.command("create-personal")
def create_personal_repos_for_all_canvas_students() -> None:
    teapot.create_personal_repos_for_all_canvas_students()


@app.command("create-teams")
def create_teams_and_repos_by_canvas_groups() -> None:
    teapot.create_teams_and_repos_by_canvas_groups()


@app.command("get-public-keys")
def get_public_key_of_all_canvas_students() -> None:
    typer.echo(teapot.get_public_key_of_all_canvas_students())


@app.command("archieve")
def archieve_all_repos() -> None:
    teapot.archieve_all_repos()


@app.command("create-issues")
def create_issue_for_repos(repo_names: List[str], title: str, body: str) -> None:
    teapot.create_issue_for_repos(repo_names, title, body)


@app.command("get-release")
def checkout_to_repos_by_release_name(
    repo_names: List[str], release_name: str, due: datetime = datetime(3000, 1, 1)
) -> None:
    teapot.checkout_to_repos_by_release_name(repo_names, release_name, due)


def run() -> None:
    app()


if __name__ == "__main__":
    run()
