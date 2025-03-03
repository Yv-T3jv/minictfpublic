#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void win() {
    printf("Congratulations! You've completed all tasks and saved the ship!\n");
    system("/bin/sh");
}

typedef struct {
    char task_name[32];
    void (*complete_task)();
} Task;

Task* tasks[10];
int task_count = 0;

void create_task() {
    if (task_count >= 10) {
        printf("Too many tasks! You can't handle more.\n");
        return;
    }

    tasks[task_count] = (Task*)malloc(sizeof(Task));
    if (!tasks[task_count]) {
        printf("Failed to allocate memory for task!\n");
        exit(1);
    }

    printf("Enter the name of the task: ");
    read(0, tasks[task_count]->task_name, 32);
    tasks[task_count]->complete_task = NULL;
    task_count++;

    printf("Task created successfully!\n");
}

void complete_task() {
    int index;
    printf("Enter the index of the task to complete: ");
    scanf("%d", &index);
    getchar(); // Consume newline

    if (index < 0 || index >= task_count || !tasks[index]) {
        printf("Invalid task index!\n");
        return;
    }

    printf("Completing task: %s\n", tasks[index]->task_name);
    if (tasks[index]->complete_task) {
        tasks[index]->complete_task();
    } else {
        printf("Task has no completion function!\n");
    }
}

void free_task() {
    int index;
    printf("Enter the index of the task to free: ");
    scanf("%d", &index);
    getchar(); // Consume newline

    if (index < 0 || index >= task_count || !tasks[index]) {
        printf("Invalid task index!\n");
        return;
    }

    free(tasks[index]);
    printf("Task freed successfully!\n");
}

void edit_task() {
    int index;
    printf("Enter the index of the task to edit: ");
    scanf("%d", &index);
    getchar(); // Consume newline

    if (index < 0 || index >= task_count || !tasks[index]) {
        printf("Invalid task index!\n");
        return;
    }

    printf("Enter the new name of the task: ");
    read(0, tasks[index]->task_name, 0x32);
    printf("Task edited successfully!\n");
}

// Main menu
void menu() {
    printf("\n--- Skeld Task Management System ---\n");
    printf("1. Create Task\n");
    printf("2. Complete Task\n");
    printf("3. Free Task\n");
    printf("4. Edit Task\n");
    printf("5. Exit\n");
    printf("> ");
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    printf("Welcome to the Skeld task management system!\n");
    printf("sus sus amongus. sus sus amongus. sus sus amongus. sus sus amongus. sus sus amongus. find the impostor. get your flag.\n");

    while (1) {
        menu();
        int choice;
        scanf("%d", &choice);
        getchar(); // Consume newline

        switch (choice) {
            case 1:
                create_task();
                break;
            case 2:
                complete_task();
                break;
            case 3:
                free_task();
                break;
            case 4:
                edit_task();
                break;
            case 5:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice!\n");
                break;
        }
    }

    return 0;
}
