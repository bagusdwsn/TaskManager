from tasks.task_manager import TaskManager

def print_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def main():
    task_manager = TaskManager()
    task_manager.load_tasks("data/tasks.json")

    while True:
        print("\nTask Manager Menu:")
        print("1. Lihat Tugas")
        print("2. Tambah Tugas")
        print("3. Tandai Selesai")
        print("4. Hapus Tugas Selesai")
        print("5. Simpan dan Keluar")

        choice = input("Pilih Menu: ")

        if choice == "1":
            tasks = task_manager.list_tasks()
            print_tasks(tasks)
        elif choice == "2":
            task_name = input("Masukkan Tugas: ")
            task_manager.add_task(task_name)
            print("Berhasil Ditambahkan.")
        elif choice == "3":
            tasks = task_manager.list_tasks()
            print_tasks(tasks)
            task_index = int(input("Masukkan Nomor Tugas Selesai: ")) - 1
            if 0 <= task_index < len(tasks):
                task_manager.complete_task(task_index)
                print("Tugas Ditandai Selesai.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            task_manager.delete_completed_tasks()
            print("Tugas Selesai Dihapus!.")
        elif choice == "5":
            task_manager.save_tasks("data/tasks.json")
            print("Tugas Tersimpan. Bye...")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main()
