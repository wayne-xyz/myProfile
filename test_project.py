from project import check_email,check_jsonfile,check_url

example1={
    "title": "Fullstack Developer | SMU MSCS",
    "bio": "Passionate about creating software and exploring new technologies.",
    "photo":"https://avatars.githubusercontent.com/u/8085091?v=4",
    "contact": {
      "email": "rongwei.ji@outlook.com",
      "linkedin": "https://www.linkedin.com/in/rongweiji",
      "github": "https://www.github.com/livingspring"
    },
    "skills": ["Swift","HTML5", "CSS3", "JavaScript", "Python", "React"],
    "projects": [
      {
        "title": "Profile Website",
        "description": "Built a personal portfolio website to showcase my skills and projects with Python and Flask",
        "url": "https://github.com/livingspring/myProfile"
      },
      {
        "title": "VoiceTranslator App",
        "description": "The Voice Translator App and Server is a project that enables users to interactively translate spoken language using their own voice, with Python, Swift, XTTS,Fastapi,iOS.",
        "url": "https://github.com/livingspring/Voice-Translator"
      }
    ]
}

example2={
    "name": "Zhangsan",
    "title": "Fullstack Developer | UTAustin MSCS",
    "bio": "Passionate about creating software and exploring new technologies.",
    "photo":"https://avatars.githubusercontent.com/u/8085091?v=4",
    "contact": {
      "email": "rongwei.ji@outlook.com",
      "linkedin": "https://www.linkedin.com/in/rongweiji",
      "github": "https://www.github.com/livingspring"
    },
    "skills": ["Swift","HTML5", "CSS3", "JavaScript", "Python", "React"],
    "projects": [
      {
        "title": "Profile Website",
        "description": "Built a personal portfolio website to showcase my skills and projects with Python and Flask",
        "url": "https://github.com/livingspring/myProfile"
      },
      {
        "title": "VoiceTranslator App",
        "description": "The Voice Translator App and Server is a project that enables users to interactively translate spoken language using their own voice, with Python, Swift, XTTS,Fastapi,iOS.",
        "url": "https://github.com/livingspring/Voice-Translator"
      }
    ]
}

example3={
    "name": "Zhangsan",
    "title": "Fullstack Developer | UTAustin MSCS",
    "bio": "Passionate about creating software and exploring new technologies.",
    "photo":"https://avatars.githubusercontent.com/u/8085091?v=4",
    "contact": {
      "email": "rongwei.ji@outlook.com",
      "linkedin": "https://www.linkedin.com/in/rongweiji",
      "github": "co"
    },
    "skills": ["Swift","HTML5", "CSS3", "JavaScript", "Python", "React"],
    "projects": [
      {
        "title": "Profile Website",
        "description": "Built a personal portfolio website to showcase my skills and projects with Python and Flask",
        "url": "https://github.com/livingspring/myProfile"
      },
      {
        "title": "VoiceTranslator App",
        "description": "The Voice Translator App and Server is a project that enables users to interactively translate spoken language using their own voice, with Python, Swift, XTTS,Fastapi,iOS.",
        "url": "https://github.com/livingspring/Voice-Translator"
      }
    ]
}

def test_check_email():
    assert check_email("nihao@")==False
    assert check_email("good")==False
    assert check_email("@good")==False
    assert check_email("hello@outlook.com")==True

def test_check_jsonfile():
    assert check_jsonfile(example1)==False
    assert check_jsonfile(example2)==True

def test_check_url():
    assert check_url(example3,["linkedin","github","url"])==False
    assert check_url(example1,["linkedin","github","url"])==True



