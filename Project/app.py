from agents.profile_agent import generate_profile


def main():

    print("\nAI PROFILE GENERATOR")
    print("=" * 50)

    name = input("Enter Name: ")
    context = input("Enter Context: ")

    result = generate_profile(
        name=name,
        context=context
    )

    print("\nPROFILE GENERATED SUCCESSFULLY")
    print(result)
    if "error" in result:
        print("\nError:")
        print(result["error"])
    else:
        print("\nOutput saved to:")
        print("output/profile.json")
        print("output/profile_*.pdf")


if __name__ == "__main__":
    main()