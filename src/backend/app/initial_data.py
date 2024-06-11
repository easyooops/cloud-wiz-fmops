from sqlmodel import Session, select
from uuid import UUID

from app.service.provider.model import Provider

def init_db(session: Session):
    initial_data = [
        {
            "company": "OpenAI",
            "name": "OpenAI",
            "description": "인간과 유사한 텍스트 생성, 번역, 요약, 질의응답 등 다양한 응용 분야에서 사용됩니다.",
            "logo": "openai.png",
            "type": "M",
            "sort_order": 1,
            "is_deleted": False,
            "creator_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
            "updater_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
        },
        {
            "company": "Anthropic",
            "name": "Anthropic",
            "description": "자연어 이해와 생성에서 높은 성능을 보이며, 윤리적 AI 개발을 중요시합니다.",
            "logo": "anthropic.png",
            "type": "M",
            "sort_order": 2,
            "is_deleted": False,
            "creator_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
            "updater_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
        },
        {
            "company": "AL21Labs",
            "name": "AL21Labs",
            "description": "산업용 애플리케이션에 주로 사용되며, 특정 도메인에서의 언어 모델 성능을 최적화합니다.",
            "logo": "openai.png",
            "type": "M",
            "sort_order": 3,
            "is_deleted": False,
            "creator_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
            "updater_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
        },
        {
            "company": "Cohere",
            "name": "Command R",
            "description": "다양한 언어 작업에 적합하며, 고성능 자연어 처리(NLP)를 목표로 합니다. 텍스트 분류, 요약, 생성 등 다양한 NLP 작업에 사용됩니다.",
            "logo": "openai.png",
            "type": "M",
            "sort_order": 4,
            "is_deleted": False,
            "creator_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
            "updater_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
        },
        {
            "company": "Amazon Web Services",
            "name": "Titan",
            "description": "다양한 언어 작업을 수행할 수 있도록 지원하며, 고성능의 NLP 기능을 제공합니다. 클라우드 인프라와 결합하여 확장성과 유연성을 자랑합니다.",
            "logo": "aws.png",
            "type": "M",
            "sort_order": 5,
            "is_deleted": False,
            "creator_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
            "updater_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
        },
        {
            "company": "Amazon Web Services",
            "name": "Amazon S3",
            "description": "다양한 파일 형식과 크기를 지원하며, 웹 기반으로 데이터를 쉽게 업로드 및 다운로드할 수 있습니다.",
            "logo": "aws.png",
            "type": "N",
            "sort_order": 1,
            "is_deleted": False,
            "creator_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
            "updater_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
        },
        {
            "company": "GIT",
            "name": "GITHub",
            "description": "Git은 분산 버전 관리 시스템으로, 모든 개발자가 전체 코드베이스의 사본을 로컬에 저장할 수 있습니다.",
            "logo": "openai.png",
            "type": "N",
            "sort_order": 2,
            "is_deleted": False,
            "creator_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
            "updater_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
        },
        {
            "company": "Notion Labs Inc",
            "name": "Notion",
            "description": "Notion은 메모, 문서 작성, 프로젝트 관리, 데이터베이스 관리 등을 하나의 플랫폼에서 할 수 있는 올인원 작업 공간을 제공합니다.",
            "logo": "openai.png",
            "type": "N",
            "sort_order": 3,
            "is_deleted": False,
            "creator_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
            "updater_id": UUID("a1eeac9b-92fb-423c-ac87-805c3266d624"),
        }
    ]

    statement = select(Provider)
    results = session.exec(statement)
    if not results.first():
        providers = [Provider(**data) for data in initial_data]
        session.add_all(providers)
        session.commit()
