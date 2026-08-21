#include <stdio.h>
#include <unistd.h>

int main(void)
{
    printf("SCADA Test Application\n");
    printf("Application is running successfully.\n");
    printf("ICS process simulation active.\n");

    while (1)
    {
        sleep(10);
    }

    return 0;
}
