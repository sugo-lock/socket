# -*- coding:utf-8 -*-
import socket

host = "127.0.0.1" #���g���̃T�[�o�[�̃z�X�g�������܂�
port = 23456 #�K����PORT���w�肵�Ă����܂�

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #�I�u�W�F�N�g�̍쐬�����܂�

client.connect((host, port)) #����ŃT�[�o�[�ɐڑ����܂�

client.send(b'Hi,Server') #�K���ȃf�[�^�𑗐M���܂��i�͂����ɂ킩��悤�Ɂj

response = client.recv(4096) #���V�[�u�͓K����2�̗ݏ�ɂ��܂��i�傫������ƃ_���j

print(response.decode())