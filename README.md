#Instrukcja obsługi aplickacji do generowania obciążenia sieci
##Istrukcja ta zawiera dokumentację aplikacji do testowania obciążenia sieci za pomocą wysyłania pakietów TCP/IP
##Spis treści:
1. Cele aplikacji
2. Struktura aplikacji
3. Klasy i ich metody
4. Obsługa aplikacji

#Cele aplikacji
Głównym celem aplikacji jest generowanie obciążenia sieci WiFi na potrzeby testowania jej wydajności.
Na tą potrzebę oprogramowanie realizuje trzy podstawowe funkcje: generowanie pakietów TCP/IP, wysyłanie pakietów pod wskazany adres i odbieranie tych pakietów.

Na potrzeby realizacji aplikacji zastosowaliśmy bibliotekę socket do wysyłania i odbierania pakietów danych.
#Struktura aplikacji
Aplikacja jest podzielona na dwa programy: server i client_sender.

Rolą programu server jest odbieranie pakietów danych. Jest on drugorzędną częścią aplikacji, ponieważ jego jedyną rolą jest zapewnienie połączenia zdolnego do odbierania wiadomości.

Program client_sender odpowiada za generowanie i wysyłanie pakietów danych. Jest on najważniejszym elementem aplikacji testowej, jako faktyczne źródło obciążenia dla sieci.

#Klasy i ich struktury
Aplikacja posiada dwie główne klasy: ISKClient i ISKServer, które odpowiadają odpowiednio za tworzenie i wysyłanie pakietów oraz ich odbiór.

##Klasa ISKClient
Klasa posiada następujące parametry:

string address - parametr address przekazywany do funkcji socket.create_connection 

int source_address - parametr source_address przekazywany do funkcji socket.create_connection

Funkcja posiada następujące metody:
__init__(self, address = 'localhost', source_address = 81) - konstruktor.

main_loop(self, iterations=10, num_of_elements = 64, wait = 0) - pętlę programu generującą i wysyłającą pakiety. Jej wykonanie zamyka połączenie. Jej parametry mają następujące znaczenie:

iterations - liczba wysłanych pakietów.

num_of_elements - rozmiar pakietów w Bajtach.

wait - odstęp między wysłanymi wiadomościami w milisekundach. Zerowy odstęp sprawia, że program wysyła wiadomości tak szybko jak to jest tylko możliwe.

##Klasa ISKServer
Klasa posiada następujące parametry:

int size - oczekiwany rozmiar przyjmowanych pakietów w Bajtach

string address - parametr address przekazywany do funkcji bind obiektu socket

int source_address - parametr source_address przekazywany do funkcji bind obiektu socket

Funkcja posiada następujące metody:
__init__(self, size = 1024, address = 'localhost', source_address = 81) - konstruktor.

main_loop(self) - tworzy socket i nasłuchuje pod zadanym adresem na zadanym porcie. Wyświetla na konsole otrzymane wiadomości. Kończy działanie dopiero po otrzymaniu sygnału przerwania.