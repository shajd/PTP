#include "stdafx.h"
#include "CustomerManagerService.h"

#define LHOST NULL
#define LPORT "42424"	
#define RECVBUFSIZE 58623

int __cdecl main()
{

	WSADATA wsaData = { 0 };
	int result = WSAStartup(MAKEWORD(2, 2), &wsaData);
	if (result != 0) {
		printf("WSAStartup failed: %d\n", result);
		return -1;
	}

	struct addrinfo hints = { 0 };
	hints.ai_family = AF_INET;
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_protocol = IPPROTO_TCP;
	hints.ai_flags = AI_PASSIVE;

	struct addrinfo *ainfo;
	result = getaddrinfo(LHOST, LPORT, &hints, &ainfo);
	if (result != 0) {
		printf("getaddrinfo failed: %d\n", result);
		WSACleanup();
		return -1;
	}

	SOCKET listenSocket;
	if ((listenSocket = socket(ainfo->ai_family, ainfo->ai_socktype, ainfo->ai_protocol)) == INVALID_SOCKET) {
		printf("socket() failed with error: %ld\n", WSAGetLastError());
		freeaddrinfo(ainfo);
		WSACleanup();
		return -1;
	}

	// Setup the TCP listening socket
	if ((bind(listenSocket, ainfo->ai_addr, (int)ainfo->ai_addrlen)) == SOCKET_ERROR) {
		printf("bind() failed with error: %d\n", WSAGetLastError());
		freeaddrinfo(ainfo);
		closesocket(listenSocket);
		WSACleanup();
		return -1;
	}
	freeaddrinfo(ainfo);

	// Listen on the socket
	if (listen(listenSocket, SOMAXCONN) == SOCKET_ERROR) {
		printf("listen() failed with error: %ld\n", WSAGetLastError());
		closesocket(listenSocket);
		WSACleanup();
		return -1;
	}

	printf("-=-=-=-=-=-=- Listening for connections -=-=-=-=-=-=- \n");
	

	while (1) {

		SOCKET clientSocket;
		if ((clientSocket = accept(listenSocket, NULL, NULL)) == INVALID_SOCKET) {
			printf("accept failed: %d\n", WSAGetLastError());
			continue;
		}
		printf("Connection received from remote host.\n");

		_beginthread(&handleConnection, 0, (void*)clientSocket);
		printf("Connection handed off to handler thread.\n");
	}
}

void __cdecl handleConnection(void *param) {
	SOCKET clientSocket = (SOCKET)param;

	char recvbuf[RECVBUFSIZE] = { '\0' };
	size_t recvbufUsed = 0;
	const char* msgPleaseSendShorterLines = "Please send shorter lines.";
	const char* msgBye = "Bye!";
	while (1) {
		size_t buf_remain = sizeof(recvbuf) - recvbufUsed;

		if (buf_remain < 1) {
			printf("[!] recvbuf exhausted. Giving up.\n");
			send(clientSocket, msgPleaseSendShorterLines, strlen(msgPleaseSendShorterLines), 0);
			break;
		}

		int result = recv(clientSocket, (void*)&recvbuf[recvbufUsed], buf_remain, 0);

		if (result == 0) {
			printf("Client disconnected.\n");
			break;
		}
		else if (result < 0) {
			printf("recv() failed: %d.\n", WSAGetLastError());
			break;
		}

		printf("Bytes received: %d\n", result);

		recvbufUsed += result;

		char *line_start = recvbuf;
		char *line_end;
		while ((line_end = (char*)memchr((void*)line_start, '\n', recvbufUsed - (line_start - recvbuf))) != 0)
		{

			*line_end = '\0';

			if (strcmp(line_start, "exit") == 0) {
				printf("Client requested exit.\n");
				send(clientSocket, msgBye, strlen(msgBye), 0);
				closesocket(clientSocket);
				return;
			}

			doResponse(clientSocket, line_start);

			line_start = line_end + 1;
		}
		
		recvbufUsed -= (line_start - recvbuf);

		memmove_s(recvbuf, sizeof(recvbuf), line_start, recvbufUsed);
	}
	closesocket(clientSocket);
	return;
}

int __cdecl doResponse(SOCKET clientSocket, char *clientName) {
	char response[128];

	sprintf(response, "ERROR %s...\n", clientName);

	int result = send(clientSocket, response, strlen(response), 0);
	if (result == SOCKET_ERROR) {
		printf("send failed: %d\n", WSAGetLastError());
		closesocket(clientSocket);
		return -1;
	}
	printf("Bytes sent: %d\n", result);
	return 0;
}