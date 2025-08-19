from textMorse import textToMorse
from morseSound import makeSound
from telegraph import run_telegraph

def main():
    print("Morse Code Converter and Sound Player")
    print("=" * 50)
    print("Choose an option:")
    print("1. Type text to convert to morse code")
    print("2. Click to write morse code directly")
    print("3. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1, 2, or 3): ").strip()
            
            if choice == "1":
                print("\n" + "=" * 30)
                print("Text to Morse Code Converter")
                print("=" * 30)
                
                # Get morse code from user input
                morse_code = textToMorse()
                
                print(f"\nMorse Code: {morse_code}")
                
                # Play the morse code sounds
                makeSound(morse_code)
                
                print("Done!")
                break
                
            elif choice == "2":
                print("\n" + "=" * 30)
                print("Telegraph Morse Code Tool")
                print("=" * 30)
                
                # Run the telegraph tool and get the morse code
                morse_code = run_telegraph()
                
                if morse_code:
                    print(f"\nMorse Code: {morse_code}")
                    print("Playing morse code sounds at 2x speed...")
                    
                    # Play the morse code sounds
                    makeSound(morse_code)
                    
                    print("Done!")
                else:
                    print("\nNo morse code entered.")
                break
                
            elif choice == "3":
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
