class BirdExpertSystem:
    def __init__(self):
        self.bird_facts = {
            'parrot': {
                'family': 'Psittacidae',
                'habitat': 'Tropical and subtropical regions',
                'diet': 'Seeds, fruits, and nuts',
                'traits': ['Colorful plumage', 'Ability to mimic human speech']
            },
            'eagle': {
                'family': 'Accipitridae',
                'habitat': 'Various habitats, including forests and mountains',
                'diet': 'Mainly carnivorous, feeding on small mammals and birds',
                'traits': ['Excellent eyesight', 'Powerful beak and talons']
            },
            'penguin': {
                'family': 'Spheniscidae',
                'habitat': 'Antarctica and other cold regions',
                'diet': 'Mainly fish and krill',
                'traits': ['Flippers for swimming', 'Thick layer of insulating feathers']
            }
        }

    def get_bird_info(self, bird_name):
        # Retrieve information about a specific bird
        bird_name = bird_name.lower()
        if bird_name in self.bird_facts:
            return self.bird_facts[bird_name]
        else:
            return None

def main():
    bird_expert = BirdExpertSystem()

    print("Welcome to the Bird Expert System!")
    print("Example queries: 'Tell me about parrot', 'What does eagle eat?', 'Traits of penguin'")
    print("Enter 'exit' to quit.")

    while True:
        user_input = input("Query: ").strip().lower()

        if user_input == 'exit':
            print("Exiting Bird Expert System.")
            break

        # Parse the user input to extract bird name and attribute
        if user_input.startswith('tell me about') or user_input.startswith('what does'):
            bird_name = user_input.split()[-1]
            bird_info = bird_expert.get_bird_info(bird_name)
            if bird_info:
                print(f"Information about '{bird_name}':")
                for key, value in bird_info.items():
                    if key == 'traits':
                        print(f"- {key.capitalize()}: {', '.join(value)}")
                    else:
                        print(f"- {key.capitalize()}: {value}")
            else:
                print(f"Sorry, information about '{bird_name}' is not available.")
        else:
            print("Invalid query format. Please try again.")

if __name__ == "__main__":
    main()
