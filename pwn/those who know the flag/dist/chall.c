#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define ARRAY_SIZE 10
#define DATA_SIZE 20

void win() {
    printf("Those who know...\n");
    system("cat flag");
    printf("Still going strong?\n");
}

void vulnerable_function() {
    char arr[ARRAY_SIZE][DATA_SIZE];  
    unsigned int pad = 0x0;
    unsigned int pad2 = 0x0;
    unsigned int secret = 0xDEADBEEF;  
    signed int index;  
    char data[DATA_SIZE];
    unsigned int *custom_ptr;

    printf("Those who know... MANGO MANGO MANGO MANGO\n");
    printf("Heres an interesting address... %p \n", (void*)&win);

    for (int i = 0; i < 2; i++) {
        printf("Enter the index to write to (%d to %d): ", 0, ARRAY_SIZE-1);
        scanf("%d", &index);
        
        printf("Enter the value to write: ");
        scanf("%s", data);

        custom_ptr = (unsigned int *)((char *)arr + index * 8);

        strcpy((char *)custom_ptr, data);

        printf("Value at custom_ptr[%d] is now: %s\n", index, (char *)custom_ptr);
    }

    if (secret != 0xCAFEBABE) {
        printf("Secret value has been modified! Exiting...\n");
        exit(1);
    } else {
        printf("Secret value is correct! Continuing...\n");
    }
}

int main() {
    
    setbuf(stdout, NULL);



    vulnerable_function();
    printf("Goodbye!\n");

    return 0;
}
