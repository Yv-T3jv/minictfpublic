#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

// ANSI color codes for visualization
#define RESET "\033[0m"
#define GREEN "\033[32m"
#define YELLOW "\033[33m"
#define BLUE "\033[34m"
#define RED "\033[31m"


// WOW! A function that prints out a flag! How cool!
void win() {
    printf(RED "You found the treasure!\n" RESET);
    printf(GREEN "Heres a flag: IRS{FAKE_FLAG}");
    exit(0);
}

// IRRELEVANT CODE
void print_stack(char *buffer_start, size_t buffer_size, uintptr_t *saved_return_addr) {
    printf("\n" YELLOW "Visualizing the Stack:\n" RESET);

    uintptr_t *start = (uintptr_t *)(buffer_start - 64); 
    uintptr_t *end = (uintptr_t *)(buffer_start + buffer_size + 64); 

    for (uintptr_t *current = start; current < end; current++) {
        uintptr_t value = *current;

        // Mark sections with labels
        if ((void *)current >= (void *)buffer_start &&
            (void *)current < (void *)(buffer_start + buffer_size)) {
            printf(BLUE "Buffer -> " RESET);
        } else if (current == saved_return_addr) {
            printf(GREEN "Return Address -> " RESET);
        } else {
            printf("              ");
        }

        printf("[%p]: 0x%lx\n", (void *)current, value);
    }
}

void vuln() {
    char buffer[40]; // <-- sus sus amongus
    uintptr_t *saved_return_addr;

#if defined(__x86_64__)
    __asm__("movq %%rbp, %0" : "=r"(saved_return_addr));
#else
    __asm__("movl %%ebp, %0" : "=r"(saved_return_addr));
#endif

    saved_return_addr += 1; 

    printf("Enter your input: ");
    fgets(buffer, 100, stdin); // <-- hmm...I can input 100 bytes when it was only allocated 40? 

    print_stack(buffer, sizeof(buffer), saved_return_addr);
}

int main() {
    vuln();
    return 0;
}

