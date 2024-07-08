-- PRAGMA foreign_keys=OFF;
START TRANSACTION;

DROP TABLE IF EXISTS alembic_version;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version VALUES('8bdb50bff9a4');

DROP TABLE IF EXISTS providers;
CREATE TABLE providers (
	provider_id CHAR(36) NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	company VARCHAR(255) NOT NULL, 
	description VARCHAR(512), 
	logo VARCHAR(255), 
	type VARCHAR(1) NOT NULL, 
	sort_order INTEGER NOT NULL, 
	is_deleted BOOLEAN NOT NULL DEFAULT 0, 
	creator_id CHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	updater_id CHAR(36),
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	PRIMARY KEY (provider_id)
);
INSERT INTO providers VALUES('21cc7c706a6a4a7c9b27c4b6b09811a7','OpenAI','OpenAI','인간과 유사한 텍스트 생성, 번역, 요약, 질의응답 등 다양한 응용 분야에서 사용됩니다.','openai.png','M',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.349599','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.349609');
INSERT INTO providers VALUES('20f21708ac19414db405a645381c7b7d','Bedrock','Amazon Web Services','AI21 Labs, Titan, Anthropic, Cohere, Meta, Mistral AI, Stability AI 등 다양한 언어 모델을 지원합니다.','aws.png','M',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.349840','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.349844');
INSERT INTO providers VALUES('68caa3424db54187aacd27159911879f','Amazon S3','Amazon Web Services','다양한 파일 형식과 크기를 지원하며, 웹 기반으로 데이터를 쉽게 업로드 및 다운로드할 수 있습니다.','aws.png','S',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.349945','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.349947');
INSERT INTO providers VALUES('739e8c581f4b494b96fe329d6d4eb2a7','GITHub','GIT','Git은 분산 버전 관리 시스템으로, 모든 개발자가 전체 코드베이스의 사본을 로컬에 저장할 수 있습니다.','openai.png','S',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.350033','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.350035');
INSERT INTO providers VALUES('8ddba5df027247b18d22ab2ae5cf4761','Notion','Notion Labs Inc','Notion은 메모, 문서 작성, 프로젝트 관리, 데이터베이스 관리 등을 하나의 플랫폼에서 할 수 있는 올인원 작업 공간을 제공합니다.','openai.png','S',3,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.350126','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.350129');
INSERT INTO providers VALUES('97137d828f3742fea081eaddd6ef4470','ChromaDB','ChromaWay','ChromaDB는 블록체인을 기반으로 한 데이터베이스로, 스마트 계약 및 탈중앙화 애플리케이션을 위한 데이터 저장 및 관리를 제공합니다.','openai.png','V',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.350221','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.350223');
INSERT INTO providers VALUES('cc7eeb0f2adb43ec8439c6b4069371c8','Pinecone','Pinecone Systems Inc','실시간 벡터 검색 및 유사성 검색을 위한 클라우드 기반 플랫폼으로, 대규모 데이터셋에서 빠르게 벡터 유사성을 탐색할 수 있습니다.','openai.png','V',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.350312','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.350314');

DROP TABLE IF EXISTS inquiry;
CREATE TABLE inquiry (
	inquiry_id INTEGER NOT NULL AUTO_INCREMENT, 
	inquiry_type VARCHAR(10) NOT NULL, 
	title VARCHAR(255) NOT NULL, 
	content TEXT NOT NULL, 
	response_content TEXT, 
	processing_type VARCHAR(255) NOT NULL, 
	is_deleted BOOLEAN NOT NULL DEFAULT 0, 
	creator_id CHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	updater_id CHAR(36),
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	PRIMARY KEY (inquiry_id)
);

DROP TABLE IF EXISTS user;
CREATE TABLE user (
	user_id CHAR(36) NOT NULL, 
	username VARCHAR(128) NOT NULL, 
	email VARCHAR(128) NOT NULL, 
	last_login DATETIME NOT NULL, 
	is_deleted BOOLEAN NOT NULL DEFAULT 0, 
	creator_id CHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	updater_id CHAR(36),
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	PRIMARY KEY (user_id)
);

DROP TABLE IF EXISTS agents;
CREATE TABLE agents (
	agent_id CHAR(36) NOT NULL, 
	user_id CHAR(36) NOT NULL, 
	agent_name VARCHAR(128) NOT NULL, 
	agent_description VARCHAR(255), 
	fm_provider_type VARCHAR(10) NOT NULL, 
	fm_provider_id CHAR(36) NOT NULL, 
	fm_model_id CHAR(36) NOT NULL, 
	fm_temperature FLOAT NOT NULL, 
	fm_top_p FLOAT NOT NULL, 
	fm_request_token_limit INTEGER NOT NULL, 
	fm_response_token_limit INTEGER NOT NULL, 
	embedding_enabled BOOLEAN NOT NULL DEFAULT 0, 
	embedding_provider_id CHAR(36), 
	embedding_model_id CHAR(36), 
	storage_provider_id CHAR(36), 
	storage_object_id CHAR(36), 
	vector_db_provider_id CHAR(36), 
	processing_enabled BOOLEAN NOT NULL DEFAULT 0, 
	pre_processing_id CHAR(36), 
	post_processing_id CHAR(36), 
	expected_request_count INTEGER NOT NULL, 
	expected_token_count INTEGER NOT NULL, 
	expected_cost FLOAT NOT NULL, 
	is_deleted BOOLEAN NOT NULL DEFAULT 0, 
	creator_id CHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	updater_id CHAR(36),
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	PRIMARY KEY (agent_id)
);
INSERT INTO agents VALUES('899e921a398b42a5aeecc6c4f0595e29','3fa85f6457174562b3fc2c963f66afa6','Default Chat Agent','Default Chat Agent Type by Cloudwiz AI FMOps','C','21cc7c706a6a4a7c9b27c4b6b09811a7','65cdd170ac3b4b7791f8911630b94ed6',0.699999999999999955,1.0,256,256,0,'21cc7c706a6a4a7c9b27c4b6b09811a7','700a3a0b7623491dbb097187b5a32fc2','68caa3424db54187aacd27159911879f','5d37242a79d942fc89de1f1b42b3cbb5',NULL,0,'063d890bb1874ab396c4e5129b79b836','352c0eac3a7148e4ac66131149bcba88',0,0,0.0,0,'3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:21:00.501862','3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:21:00.501864');
INSERT INTO agents VALUES('409dbb5d8e9940f3b17050400f0fd249','3fa85f6457174562b3fc2c963f66afa6','Default Text Agent','Default Text Agent Type by Cloudwiz AI FMOps','T','21cc7c706a6a4a7c9b27c4b6b09811a7','e9a9e4404a4746e497f6d8cd0035128f',0.699999999999999955,1.0,256,256,0,'21cc7c706a6a4a7c9b27c4b6b09811a7','700a3a0b7623491dbb097187b5a32fc2','68caa3424db54187aacd27159911879f','5d37242a79d942fc89de1f1b42b3cbb5',NULL,0,'063d890bb1874ab396c4e5129b79b836','352c0eac3a7148e4ac66131149bcba88',0,0,0.0,0,'3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:21:00.513269','3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:21:00.513272');

DROP TABLE IF EXISTS models;
CREATE TABLE models (
	model_id CHAR(36) NOT NULL, 
	model_name VARCHAR(255) NOT NULL, 
	provider_id CHAR(36) NOT NULL, 
	model_type VARCHAR(10) NOT NULL, 
	sort_order INTEGER NOT NULL, 
	is_deleted BOOLEAN NOT NULL DEFAULT 0, 
	creator_id CHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	updater_id CHAR(36),
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	PRIMARY KEY (model_id)
);
INSERT INTO models VALUES('65cdd170ac3b4b7791f8911630b94ed6','gpt-3.5-turbo','21cc7c706a6a4a7c9b27c4b6b09811a7','C',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.383933','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.383936');
INSERT INTO models VALUES('9465af2409b143f1a88f8d0364d12227','gpt-4','21cc7c706a6a4a7c9b27c4b6b09811a7','C',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.384632','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.384635');
INSERT INTO models VALUES('d0b8dbf8f6a440efa043ca7a4d7aa950','gpt-4-turbo','21cc7c706a6a4a7c9b27c4b6b09811a7','C',3,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.385194','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.385196');
INSERT INTO models VALUES('dfb7fea4afb346e38b3b6345e1ea8e0f','gpt-4o','21cc7c706a6a4a7c9b27c4b6b09811a7','C',4,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.385704','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.385707');
INSERT INTO models VALUES('70fdf54470ed4c7396db144f010ec998','dall-e-2','21cc7c706a6a4a7c9b27c4b6b09811a7','I',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.386209','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.386211');
INSERT INTO models VALUES('a6ed4c0fee1a44a48c68cdaa33d267e9','dall-e-3','21cc7c706a6a4a7c9b27c4b6b09811a7','I',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.386713','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.386716');
INSERT INTO models VALUES('30b3ec08c5b74d9cb60d59b44f4f3231','tts-1-hd','21cc7c706a6a4a7c9b27c4b6b09811a7','S',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.387241','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.387243');
INSERT INTO models VALUES('caa8188588844ab58c42447ac51484e4','tts-1','21cc7c706a6a4a7c9b27c4b6b09811a7','S',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.387760','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.387762');
INSERT INTO models VALUES('f4ace494cbc24635abe9349c463a1d1f','whisper-1','21cc7c706a6a4a7c9b27c4b6b09811a7','S',3,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.388398','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.388401');
INSERT INTO models VALUES('700a3a0b7623491dbb097187b5a32fc2','text-embedding-ada-002','21cc7c706a6a4a7c9b27c4b6b09811a7','E',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.389003','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.389005');
INSERT INTO models VALUES('f5d8b1dcb36e4e49b8f7911c99c18a38','text-embedding-3-small','21cc7c706a6a4a7c9b27c4b6b09811a7','E',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.389670','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.389672');
INSERT INTO models VALUES('6c57a89f633c484397fbb850f915f5dc','text-embedding-3-large','21cc7c706a6a4a7c9b27c4b6b09811a7','E',3,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.390179','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.390181');
INSERT INTO models VALUES('7044b565363d4b4c8f40dbf97841d73a','davinci-002','21cc7c706a6a4a7c9b27c4b6b09811a7','T',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.390693','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.390695');
INSERT INTO models VALUES('07b2b4de145d4813a2c701d19f34501f','babbage-002','21cc7c706a6a4a7c9b27c4b6b09811a7','T',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.391183','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.391186');
INSERT INTO models VALUES('2bd3281a4d7641aa91edb7a208ed9498','text-moderation-007','21cc7c706a6a4a7c9b27c4b6b09811a7','T',3,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.391818','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.391822');
INSERT INTO models VALUES('58955d2012824b9fa943d9352b2be5ea','text-moderation-stable','21cc7c706a6a4a7c9b27c4b6b09811a7','T',4,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.392685','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.392692');
INSERT INTO models VALUES('aa599305934e4cc79ca411e11dda534e','text-moderation-latest','21cc7c706a6a4a7c9b27c4b6b09811a7','T',5,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.394331','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.394337');
INSERT INTO models VALUES('e9a9e4404a4746e497f6d8cd0035128f','gpt-3.5-turbo-instruct','21cc7c706a6a4a7c9b27c4b6b09811a7','T',6,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.395776','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.395785');
INSERT INTO models VALUES('7290ae9cae2446ffa31bfb0a2f579d33','ai21.j2-ultra-v1','20f21708ac19414db405a645381c7b7d','T',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.397370','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.397376');
INSERT INTO models VALUES('c0c088aaabd944b4878ebfdc85efcbc3','ai21.j2-mid-v1','20f21708ac19414db405a645381c7b7d','T',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.398560','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.398566');
INSERT INTO models VALUES('fff83a9fe1684234b01d4dad4b355547','amazon.titan-embed-text-v1','20f21708ac19414db405a645381c7b7d','E',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.399461','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.399465');
INSERT INTO models VALUES('98eec999ba994aa28831d7655539d888','amazon.titan-text-lite-v1','20f21708ac19414db405a645381c7b7d','T',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.400248','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.400252');
INSERT INTO models VALUES('0671a2aeeba54b368d866619028d4d9e','amazon.titan-text-express-v1','20f21708ac19414db405a645381c7b7d','C',3,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.400912','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.400916');
INSERT INTO models VALUES('55340687de724e18a765c111cdcddb4a','amazon.titan-image-generator-v1','20f21708ac19414db405a645381c7b7d','I',4,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.401946','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.401954');
INSERT INTO models VALUES('d53ca0ee65f345da94a6a62a94ef8739','amazon.titan-embed-image-v1','20f21708ac19414db405a645381c7b7d','E',5,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.403205','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.403211');
INSERT INTO models VALUES('5b9dea8d802946d5a1ff08d036539c67','amazon.titan-text-premier-v1:0','20f21708ac19414db405a645381c7b7d','C',6,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.403893','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.403896');
INSERT INTO models VALUES('9fb038cae47747dd800cd824f2e80031','amazon.titan-embed-text-v2:0','20f21708ac19414db405a645381c7b7d','E',7,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.404599','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.404602');
INSERT INTO models VALUES('7d8e9ca9bf7042678e715eebd472b37d','anthropic.claude-3-sonnet-20240229-v1:0','20f21708ac19414db405a645381c7b7d','C',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.405285','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.405289');
INSERT INTO models VALUES('975f5fcbae884a6aa5189909338094b9','anthropic.claude-3-haiku-20240307-v1:0','20f21708ac19414db405a645381c7b7d','C',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.406253','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.406258');
INSERT INTO models VALUES('046e9ec9f5cb4d19869ff3a228e7cb68','anthropic.claude-v2:1','20f21708ac19414db405a645381c7b7d','C',3,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.407155','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.407160');
INSERT INTO models VALUES('75396664a17a405fb0976c19efac0b16','anthropic.claude-v2','20f21708ac19414db405a645381c7b7d','C',4,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.408049','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.408053');
INSERT INTO models VALUES('51b2f4577c714bada2d6d1df86480dd9','anthropic.claude-instant-v1','20f21708ac19414db405a645381c7b7d','C',5,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.409656','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.409667');
INSERT INTO models VALUES('bb663f2ac1e04ef3a55e2c289aba1cc7','cohere.command-r-plus-v1:0','20f21708ac19414db405a645381c7b7d','T',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.410940','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.410946');
INSERT INTO models VALUES('254927f94fd0453292b2f904e1f17d3b','cohere.command-r-v1:0','20f21708ac19414db405a645381c7b7d','T',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.412210','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.412218');
INSERT INTO models VALUES('711a1c26c9484a25a44e2364cc9cd2e6','cohere.embed-english-v3','20f21708ac19414db405a645381c7b7d','E',3,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.413758','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.413766');
INSERT INTO models VALUES('9b70fb1433994d628ea2e00d58ea6a86','cohere.embed-multilingual-v3','20f21708ac19414db405a645381c7b7d','E',4,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.415033','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.415039');
INSERT INTO models VALUES('d42fe162aaac4a9889caa49ccd7bfa53','cohere.command-text-v14','20f21708ac19414db405a645381c7b7d','T',5,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.416347','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.416356');
INSERT INTO models VALUES('9d490374b47e4216844797e634c6b28b','cohere.command-light-text-v14','20f21708ac19414db405a645381c7b7d','T',6,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.417967','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.417975');
INSERT INTO models VALUES('ec4b12100d44414cb5b8637fa5df8cce','meta.llama3-8b-instruct-v1:0','20f21708ac19414db405a645381c7b7d','T',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.419405','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.419412');
INSERT INTO models VALUES('ebcc49dcec6d4298ac0bd6ebf47a3a9e','meta.llama3-70b-instruct-v1:0','20f21708ac19414db405a645381c7b7d','T',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.420270','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.420273');
INSERT INTO models VALUES('194fb0cd412b4f7d98907cb4d4d31359','meta.llama2-13b-chat-v1','20f21708ac19414db405a645381c7b7d','C',3,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.421068','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.421073');
INSERT INTO models VALUES('2948ae5c98ad4149bdf76e1ed93c7123','meta.llama2-70b-chat-v1','20f21708ac19414db405a645381c7b7d','C',4,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.422083','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.422088');
INSERT INTO models VALUES('739d6963f0dd447cb2b8d46692a63fe0','mistral.mistral-7b-instruct-v0:2','20f21708ac19414db405a645381c7b7d','T',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.423104','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.423108');
INSERT INTO models VALUES('bb38a96c3c0144e6b2a8e58cb85eaa37','mistral.mixtral-8x7b-instruct-v0:1','20f21708ac19414db405a645381c7b7d','C',2,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.424103','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.424108');
INSERT INTO models VALUES('61b61987a2e3419fbc17519fbb153716','mistral.mistral-large-2402-v1:0','20f21708ac19414db405a645381c7b7d','T',3,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.425065','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.425070');
INSERT INTO models VALUES('54988c32ca244d0b8ff930ca532e98f3','mistral.mistral-small-2402-v1:0','20f21708ac19414db405a645381c7b7d','T',4,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.426053','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.426059');
INSERT INTO models VALUES('e69962b42dd34dd08da5b663aa6a0f59','stability.stable-diffusion-xl-v1','20f21708ac19414db405a645381c7b7d','I',1,0,'a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.427510','a1eeac9b92fb423cac87805c3266d624','2024-07-08 09:20:57.427517');

DROP TABLE IF EXISTS chain;
CREATE TABLE chain (
	chain_id CHAR(36) NOT NULL, 
	agent_id CHAR(36) NOT NULL, 
	provider_id CHAR(36) NOT NULL, 
	connection_order INTEGER NOT NULL, 
	is_deleted BOOLEAN NOT NULL DEFAULT 0, 
	creator_id CHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	updater_id CHAR(36),
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (chain_id)
);

DROP TABLE IF EXISTS credentials;
CREATE TABLE credentials (
	credential_id CHAR(36) NOT NULL, 
	user_id CHAR(36) NOT NULL, 
	provider_id CHAR(36) NOT NULL, 
	credential_name VARCHAR(255) NOT NULL, 
	access_key VARCHAR(125), 
	secret_key VARCHAR(125), 
	session_key VARCHAR(125), 
	access_token VARCHAR(125), 
	api_key VARCHAR(125), 
	api_endpoint VARCHAR(255), 
	is_deleted BOOLEAN NOT NULL DEFAULT 0, 
	creator_id CHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	updater_id CHAR(36),
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (credential_id)
);
INSERT INTO credentials VALUES('c2c268f7de3e463c9e57f98d06506c25','3fa85f6457174562b3fc2c963f66afa6','21cc7c706a6a4a7c9b27c4b6b09811a7','Default OpenAI','','','','','1231231231231','',0,'3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:20:57.456693','3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:20:57.456697');
INSERT INTO credentials VALUES('9879a5a662064c1fbafefc49ddb90e69','3fa85f6457174562b3fc2c963f66afa6','20f21708ac19414db405a645381c7b7d','Default Bedrock','1231231231231','1231231231231','1231231231231','','','',0,'3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:20:57.457629','3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:20:57.457632');
INSERT INTO credentials VALUES('742f4ce7c3454010af43f0f036344dbe','3fa85f6457174562b3fc2c963f66afa6','68caa3424db54187aacd27159911879f','Default Amazon S3','1231231231231','1231231231231','1231231231231','','','',0,'3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:20:57.458415','3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:20:57.458420');

DROP TABLE IF EXISTS store;
CREATE TABLE store (
	store_id CHAR(36) NOT NULL, 
	user_id CHAR(36) NOT NULL, 
	store_name VARCHAR(255) NOT NULL, 
	description VARCHAR(255), 
	is_deleted BOOLEAN NOT NULL DEFAULT 0, 
	creator_id CHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	updater_id CHAR(36),
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (store_id)
);
INSERT INTO store VALUES('5d37242a79d942fc89de1f1b42b3cbb5','3fa85f6457174562b3fc2c963f66afa6','Default Storage','Default Storage with Cloudwiz AI FMOps',0,'3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:21:00.213110','3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:21:00.213122');

DROP TABLE IF EXISTS processing;
CREATE TABLE processing (
	processing_id CHAR(36) NOT NULL, 
	user_id CHAR(36) NOT NULL, 
	processing_type VARCHAR(10) NOT NULL, 
	processing_name VARCHAR(255) NOT NULL, 
	processing_desc VARCHAR(255), 
	template TEXT, 
	pii_masking VARCHAR(512), 
	normalization VARCHAR(512), 
	stopword_removal TEXT, 
	is_deleted BOOLEAN NOT NULL DEFAULT 0, 
	creator_id CHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	updater_id CHAR(36),
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (processing_id)
);
INSERT INTO processing VALUES('063d890bb1874ab396c4e5129b79b836','3fa85f6457174562b3fc2c963f66afa6','pre','Default Pre-Processing','Default Pre-Processing by Cloudwiz AI FMOps',replace('"""\nQuestion: {question}\nContext: Summarize it\nAnswer: Let`s think step by step.\n"""','\n',char(10)),'','','CLOUDWIZ|AI|FMOPS',0,'3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:21:00.473859','3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:21:00.473862');
INSERT INTO processing VALUES('352c0eac3a7148e4ac66131149bcba88','3fa85f6457174562b3fc2c963f66afa6','post','Default Post-Processing','Default Post-Processing by Cloudwiz AI FMOps',replace('"""\nQuestion: {question}\nContext: Summarize it\nAnswer: Let`s think step by step.\n"""','\n',char(10)),'','','CLOUDWIZ|AI|FMOPS',0,'3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:21:00.473966','3fa85f6457174562b3fc2c963f66afa6','2024-07-08 09:21:00.473967');
CREATE INDEX ix_providers_provider_id ON providers (provider_id);
CREATE INDEX ix_providers_company ON providers (company);
CREATE INDEX ix_providers_name ON providers (name);
CREATE INDEX ix_providers_description ON providers (description);
CREATE INDEX ix_inquiry_title ON inquiry (title);
CREATE INDEX ix_inquiry_id ON inquiry (inquiry_id);
CREATE INDEX ix_inquiry_inquiry_type ON inquiry (inquiry_type);
CREATE INDEX ix_user_user_id ON user (user_id);
CREATE INDEX ix_user_email ON user (email);
CREATE INDEX ix_user_username ON user (username);
CREATE INDEX ix_agents_fm_model_id ON agents (fm_model_id);
CREATE INDEX ix_agents_user_id ON agents (user_id);
CREATE INDEX ix_agents_fm_provider_id ON agents (fm_provider_id);
CREATE INDEX ix_agents_agent_id ON agents (agent_id);
CREATE INDEX ix_models_provider_id ON models (provider_id);
CREATE INDEX ix_models_model_type ON models (model_type);
CREATE INDEX ix_models_model_name ON models (model_name);
CREATE INDEX ix_models_model_id ON models (model_id);
CREATE INDEX ix_chain_chain_id ON chain (chain_id);
CREATE INDEX ix_credentials_user_id ON credentials (user_id);
CREATE INDEX ix_credentials_credential_id ON credentials (credential_id);
CREATE INDEX ix_credentials_provider_id ON credentials (provider_id);
CREATE INDEX ix_store_store_id ON store (store_id);
CREATE INDEX ix_store_user_id ON store (user_id);
CREATE INDEX ix_processing_user_id ON processing (user_id);
CREATE INDEX ix_processing_processing_id ON processing (processing_id);
COMMIT;
