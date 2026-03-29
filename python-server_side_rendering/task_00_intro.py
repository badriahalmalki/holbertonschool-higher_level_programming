def generate_invitations(template, attendees):
    # Validate template type
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    # Validate attendees type
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of template
        output = template

        # Replace placeholders
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for key in placeholders:
            value = attendee.get(key)

            # Handle missing or None values
            if value is None:
                value = "N/A"

            output = output.replace(f"{{{key}}}", str(value))

        # Write to file
        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(output)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
