/*

	Program    : Inter Process Communication
	Status     : Completed
	Created by : Sarath Peter
*/

// Header files here

#include<unistd.h>
#include<stdio.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/stat.h>

// Definitions here
#define MAX_LIMIT 100

// Functions here


// Program Main
void main()
{
 int id,desc,i,pp[2],pc[2];
 char buff[50];
 pipe(pp);
 pipe(pc);
 id=fork();
 if(id==0)
 {
   printf("\n\n\nIPC using Unnmad double Piped (via System Call)\n\n");
   printf("\n............CHILD says: Enter data to parent:.\n");
   gets(buff);
   write(pp[1],buff,50);
   printf("\n............child says:Data from parent is \n");
   puts(buff);
 }
 else
 {
  sleep(1);
  read(pp[0],buff,50);
  printf("\n........parent says:Data from child is:\n");
  puts(buff);
  printf("\n..........PARENT says:enter data to child:\n");
  gets(buff);
  write(pc[1],buff,50);
  wait(0);
  read(pc[0],buff,i);
  printf("\n.........PARENT says:Data in pipe:\n");
  write(STDOUT_FILENO,buff,i);
  printf("\n\n");
 }
}
