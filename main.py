import sys
import os

def print_header():
    print("=" * 65)
    print("      RUT-SIM: Resonant Universe Theory Simulation Suite")
    print("=" * 65)
    print("1. Фазовый портрет устойчивости вакуумного резонатора (2D)")
    print("2. 3D-топология солитонов в 6D (n=1,2,3,4)")
    print("3. Расчет матриц смешивания CKM и PMNS")
    print("4. Запустить все модули последовательно")
    print("0. Выход")
    print("=" * 65)

def main():
    while True:
        print_header()
        choice = input("Выберите модуль (0-4): ").strip()
        
        if choice == '1':
            print("\n[Запуск модуля потенциала вакуума...]")
            os.system("python3 sci.py")
        elif choice == '2':
            print("\n[Запуск 3D-визуализации солитонов...]")
            os.system("python3 soliton_3d.py")
        elif choice == '3':
            print("\n[Запуск расчета углов смешивания CKM/PMNS...]")
            os.system("python3 mixing_matrices.py")
        elif choice == '4':
            print("\n[Последовательный запуск всего комплекса...]")
            os.system("python3 sci.py")
            os.system("python3 soliton_3d.py")
            os.system("python3 mixing_matrices.py")
        elif choice == '0':
            print("\nЗавершение работы RUT-SIM.")
            sys.exit(0)
        else:
            print("\nНеверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
