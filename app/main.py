def copy_file(command: str) -> None:
    try:
        com, file_from, new_file = command.split()
        if com == "cp" and file_from != new_file:
            with (
                open(file_from, "r") as file_in,
                open(new_file, "w") as file_out
            ):
                file_out.write(file_in.read())
        else:
            pass
    except Exception:
        pass
