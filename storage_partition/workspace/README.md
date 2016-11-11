File Storage Service


A client can create a directory with the name of his choice. When the directory is successfully stored he gets a unique directory id for the stored directory. A client can also store a file with a name of his choice in directory of his choice. When the file is successfully stored he gets a unique file id for the stored file3. A client can also remove any of his stored files by providing the name or id of the file and the name or id of the directory.

If a client attempts to store a file with a name with which a file already exists in the directory, the the previous file gets overridden. A client is also able to retrieve any of his stored files from a directory by providing the name or id of the file and the directory.

A client can also retrieve the list of names of his stored files in a directory. A client can also retrieve list of names of his stored directories.

Each client has a storage quota of 1GB, which means the total size of his stored files cannot exceed 1 GB.

Each client has a bandwidth quota of 10 GB, which means the total data transfer he does while storing files cannot exceed 10 GB. So if a client stores 1 GB of data and then removes it and again stores 1 GB of data, he has used 2 GB of bandwidth.
