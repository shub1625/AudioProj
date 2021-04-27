# AudioProj
Django Web API that simulates the behavior of an audio file

1. API End-points : 

        (audioFileType = songs / podcasts / audiobooks
         audioFildId = primary key(pk) )

        'List': '/audioFileType/',
        'Detail View': '/audioFileType/audioFildId',
        'Create' : '/create/',
        'Update' : '/update/audioFileType>/audioFildId/',
        'Delete' : '/delete/audioFileType>/audioFildId/'

2. Datebase : Postgres

3. Sample Inputs :
    1. Create :
        a. Song:
            {
	            "audioFileType": "song",
	             "audioFileMetadata" : {	"duration_time" : "60",
							"uploaded_time" : "2021-04-27T00:38:01+05:30",
							"name" : "Blank  Space"							
						}
            }

        b. PODCAST:
            {
	            "audioFileType": "podcast",
	            "audioFileMetadata" : {	"duration_time" : "60",
							"uploaded_time" : "2021-04-28T00:38:01+05:30",
							"name" : "Blank  Space",
							"host": "Renni Eddo",
							"participents": [ "John", "Rance", "Jack" ]
						}
            }

        c. AudioBook:
            {
	            "audioFileType": "audiobook",
	            "audioFileMetadata" : {	"duration_time" : "60",
							"uploaded_time" : "2021-04-28T00:38:01+05:30",
							"title" : "Wilderness",
							"author": "Tom Eddo",
							"narrator": "Jimmy"
			            }
            }
    

4. Validatiors : 
    1. All model field related validations 
    2. Uploaded time cannot be past date custom validation
