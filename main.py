from models import Calculator


def display_menu():
    """Display the calculator menu options."""
    print("\n" + "="*40)
    print("       КАЛКУЛАТОР - ГЛАВНО МЕНЮ")
    print("="*40)
    print("1. Събиране (+)")
    print("2. Изваждане (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Вижте текущия резултат")
    print("6. Вижте историята на операциите")
    print("7. Нулиране на калкулатора")
    print("8. Изход")
    print("="*40)


def main():
    """Main application function."""
    calc = Calculator()

    
    while True:
        display_menu()
        choice = input("Изберете опция (1-8): ").strip()
        
        try:
            if choice == "1":
                number = float(input("Въведете число за събиране: "))
                result = calc.add(number)
                print(f"✓ Резултат: {result}")
            
            elif choice == "2":
                number = float(input("Въведете число за изваждане: "))
                result = calc.subtract(number)
                print(f"✓ Резултат: {result}")
            
            elif choice == "3":
                number = float(input("Въведете число за умножение: "))
                result = calc.multiply(number)
                print(f"✓ Резултат: {result}")
            
            elif choice == "4":
                number = float(input("Въведете число за деление: "))
                result = calc.divide(number)
                print(f"✓ Резултат: {result}")
            
            elif choice == "5":
                current = calc.get_result()
                print(f"\nТекущ резултат: {current}\n")
            
            elif choice == "6":
                history = calc.get_history()
                if history:
                    print("\n📋 ИСТОРИЯ НА ОПЕРАЦИИТЕ:")
                    for i, operation in enumerate(history, 1):
                        print(f"  {i}. {operation}")
                    print()
                else:
                    print("\n⚠️  Няма операции в историята.\n")
            
            elif choice == "7":
                calc.reset()
                print("✓ Калкулаторът е нулиран.")
            
            elif choice == "8":
                print("\nСпасибо за използването на калкулатора! До виждане! 👋\n")
                break
            
            else:
                print("❌ Невалиден избор. Моля, изберете 1-8.")
        
        except ValueError as e:
            print(f"❌ Грешка: {e}. Моля, въведете валидно число.")
        except Exception as e:
            print(f"❌ Възникна грешка: {e}")


if __name__ == "__main__":
    main()
