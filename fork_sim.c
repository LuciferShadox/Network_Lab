/*

	Program    : Fork Implementation
	Status     : Stable
	Created by : Sarath Peter
*/

// Header files here

#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
// Definitions here
#define MAX_LIMIT 100

// Functions here

void child(int id)
{
	printf("\nProcess  %d : Now Children will do something",id);
}

void parent(int id)
{
	printf("\nProcess %d : Now Parent is doing something",id);
}

// Program Main
void main()
{
	system("clear");

        pid_t id;
	id=fork();

	if(id==0)
	{
		child(id);
	}
	else if(id>0)
	{
		parent(id);
	}
	else
	{
		printf("\n Nothing happend");
	}
	printf("\n");
}
