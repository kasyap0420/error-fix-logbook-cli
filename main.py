from app.menu import run_app


if __name__ == "__main__":
    try:
        run_app()
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")