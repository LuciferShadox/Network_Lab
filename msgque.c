/*

	Program    :  Message Queue implementation
	Status     :  Developing
	Created by :  Sarath Peter
*/

// Header files here

#include<stdio.h>
#include<stdlib.h>
#include<sys/type.h>
#include<sys/msg.h>
#include<sys/ipc.h>
#include<string.h>

// Definitions here
#define MAX_LIMIT 100

struct MESSAGE
{
  long id;
	char usrID[26],content[200];
}

// Functions here
int c2n(char str[])
{
	 int i,x=1,r=0;
	 for(i=0;i<strlen(str);i++)
	 {
		 r+=x*toascii(str[i]);
		 x*=10;
	 }

	 return r;
}

int sender(int qid,char str[])
{
	strut MESSAGE m;
  strcpy(m.usrID, str);
	m.id = c2n(str);

	printf("\nMessage : \n");
	scanf("%s",m.content);

	if(msgsnd(qid,&m,sizeof(m),0) < 0)
	{
		system("clear");
		perror("M%d : Failed to send message \n",qid);
	}

  else
	{
		 printf("Message sent\n");
	}

}

int recciver(int qid,char str[])
{
  struct MESSAGE m;
	long id = c2n(name);

		printf("\n Message Reccived :");
		if(msgrcv(qid,&m,sizeof(m),id,0)<0)
		{
			system("clear");
			perror("M%d : Failed to recive message \n",qid);
		}
		else
		{
			printf("%s",m.content);
		}

}

// Program Main
void main()
{

	int a,b,qid,msgid,opt;
	char
}
