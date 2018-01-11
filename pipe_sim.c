/*

	Program    : Pipe Implementation
	Status     : Developing
	Created by : Sarath Peter
*/

// Header files here

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

// Definitions here

#define MAX_LIMIT 100
#define SUCESS " GOT THE MESSAGE \n"
#define FAIL   " DIDNT GET THE MESSAGE \n"
char MSG_BUF[MAX_LIMIT];

// Functions here

void GET_MSG(void)
{
	printf("Message : ");
	scanf("%s",MSG_BUF);
}

// Program Main
void main()
{
  pid_t ID_USER;
  char buffer[MAX_LIMIT],status[MAX_LIMIT];
  int pass[2],ret[2],BYTE_SIZE;

  system("clear");
  
  pipe(pass);
  ID_USER = fork();
  
  if(ID_USER == 0)
  {
	GET_MSG();
	write(pass[1],MSG_BUF,MAX_LIMIT);
        read(ret[0],status,sizeof(SUCESS));
  	close(pass[1]);
  }	
  
  else
  {	
	BYTE_SIZE = read(pass[0],buffer,MAX_LIMIT);
	if(BYTE_SIZE != NULL){
		printf("String : %s ",buffer);
		write(ret[1],SUCESS,sizeof(SUCESS));		
		close(pass[0]);
	}
	else{
		write(ret[1],FAIL,sizeof(FAIL));
		exit(0);	
	}
  }

 printf("\n\n-- Break -- \n\n");
}
