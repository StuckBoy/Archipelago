# Dark Souls Remastered Randomizer Setup Guide

## Required Software

- [Dark Souls Remastered](https://store.steampowered.com/app/570940/DARK_SOULS_REMASTERED/)
- [Dark Souls Remastered AP Client]() (Update before beta test.)

## Optional Software

- [Dark Souls Remastered Tracker Pack](https://github.com/MagoMerlin/MagoMerlin.github.io#dark-souls-randomizer-tracker)

## General Concept

The AP client for Dark Souls Remastered is implemented as a dinput8.dll that is loaded when launching Dark Souls 
Remastered. A command prompt will appear where you can view information about the run and interact with the Archipelago
server using specific commands.

## Installation Procedure

*Use of this mod while online may result in a ban from the FromSoftware servers.*

This client has been written and tested against the official Steam version of the game (v1.03.1/1.04).

Obtain the dinput8.dll from the [Dark Souls Remastered AP Client]() repository and place it in the root folder of your
Dark Souls Remastered installation (i.e. SteamLibrary\steamapps\common\DARK SOULS REMASTERED\).

## Joining a MultiWorld Game

1. Run Dark Souls Remastered through Steam, the command prompt should open as well
2. Type in `/connect {SERVER_IP}:{SERVER_PORT} {SLOT_NAME}` in the command prompt that opened while on the main menu
3. Once connected, create a new game, choose a class and begin

To rejoin an active MultiWorld, simply follow the steps above prior to loading your game from the main menu.

## Where do I get a config file?

The [Player Settings](/games/Dark%Souls%Remastered/player-settings) page on the website allows you to configure your 
personal settings and export them into a config file for later use.