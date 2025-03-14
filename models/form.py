class Form:
    # Static method to display a form and execute the corresponding function based on the user's choice
    @staticmethod
    def display(title: str, choices: list[str], functions: list[callable]):
        """
        Displays a form with a title and choices, and executes the function corresponding to the user's choice.

        :param title: The title to display at the top of the form.
        :param choices: A list of strings representing the available choices.
        :param functions: A list of functions to execute corresponding to the choices.
        """
        # Print the title
        print(f"\n{title}")

        # Print the choices
        for index, choice in enumerate(choices, start=1):
            print(f"{index}: {choice}")

        # Get the user's input
        try:
            user_input = int(input("\nChoisis une option: "))

            # Check if the input is within the range of available choices
            if 1 <= user_input <= len(choices):
                # Execute the corresponding function
                return functions[user_input - 1]()
            else:
                print("Choix invalide, veuillez réessayer.")
                Form.display(title, choices, functions)  # Re-display the form if the input is invalid

        except ValueError:
            print("Veuillez entrer un numéro valide.")
            Form.display(title, choices, functions)  # Re-display the form in case