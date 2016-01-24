# Wheaton Life Server

This is the server side of the wheaton Life app (will under construction after all the api's are finished)

## What This Will be Like

This server app WILL(not now) contain the api of
 
 1. Gatra 140 time table
 
 2. MBTA (Boston Providence line) schedule
 
 3. the availability of washing machine
 
-

There will be 2 kind of api's:

 1. real-time updated api: every time you create a request, the server scrubs the website, send the data to you and create a cache
 
 2. cached api: the server will not scrub the website, it will just send you the latest cache in the server, if the cache haven't update in certain timeout time, the server will update the cache

-

if your apps need accurate data, please use the real-time api, if you need super fast speed(scrub will take less than couple second), you can use the cache api
    
if there is other api's needed, please submit an issue contact me, I will consider adding them.(or just write it yourself, and create a pull request)

###* But for now you cannot use this code to do anything... oooops...*

## Notice

All the data is acquired from the internet, if there any right violation, please submit an issue or contact me.

## Construction Road Map:
1/24/2016: the scraber for gatra 140 site is finished

## TODOS:

1. finish the scraber for MBTA

2. finish the api's for transportation(both MBTA and gatra)

3. finish the scraber for washing machine (whatever it called)

4. finish the api for waching machine

5. finish the c# wrapper for this api
