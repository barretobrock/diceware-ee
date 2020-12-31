#/ Basic operation of the password generation script

LIMIT=${1}

python3 ./sonad.py -c ${LIMIT}

printf "\n------\nGenerated Secrets with limit ${LIMIT}:\n------\n"
cat ./output