class UserService:

    @staticmethod
    def get_welcome_message(first_name: str) -> str:
        return (
            f"Welcome, {first_name}!\n\n"
            "Your Telegram bot is running.\n"
            "Use /help to see available commands."
        )