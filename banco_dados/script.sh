#! /bin/sh
mongoimport -d bigdata -c formularios --type csv --file formulario.csv --headerline
