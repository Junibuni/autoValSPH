## 설치

### 1. 가상 환경 만들기
가상 환경을 만듭니다:

```bash
python -m venv venv
```

### 2. 가상 환경 활성화
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. 의존성 설치
다음 명령어로 필요한 라이브러리를 설치합니다:

```bash
pip install -r requirements.txt
```

## SPH3D Solver 설정 파일

이 파일은 **SPH3D Solver** 실행을 위한 샘플 JSON 설정 파일입니다. 주요 구성 요소와 사용 방법을 설명합니다.

---

### JSON 파일 구성

```json
{
    "name": "홍길동 주임연구원",
    "commit_number": "SPH3D/dg1ldj",
    "solver_pth" : "D:/sources/VSBuild/x64/Release/RuntimeSPH.exe",
    "val_folder_pth": "D:/sources/test_files/Validation",
    "log_pth": "",
    "settings": {
            "VAL_Hydro_Static": {
                "grid_number": 1
            },
            "VAL_Dam_Break": {
                "grid_number": 1
            },
            "VAL_OBC_Poiseuille": {
                "grid_number": 1
            },
            "VAL_Periodic_Poiseuille": {
                "grid_number": 1
            }
    }
}
```

---

### 필드 설명

- **name**: 사용자 이름 또는 실행 담당자 (예: `"홍길동 주임연구원"`).
- **commit_number**: 사용한 코드의 특정 커밋 번호를 명시 (예: `"SPH3D/dg1ldj"`).
- **solver_pth**: 실행할 SPH Solver 실행 파일의 경로.
- **val_folder_pth**: Validation 테스트 파일이 위치한 폴더 경로.
- **log_pth**: 로그 파일 경로 (지정하지 않으면 현재 디렉토리에 자동 설정).
- **settings**: 실행할 해석 설정.

---

### `settings` 내부 구조

`settings`에는 수행할 해석 유형과 추출할 데이터의 `grid_number`를 지정할 수 있습니다.

| 해석 이름                  | 설명                                | grid_number 예제 |
|---------------------------|--------------------------------|-----------------|
| `VAL_Hydro_Static`        | 정수압 시뮬레이션              | `1`             |
| `VAL_Dam_Break`           | 댐 붕괴 시뮬레이션                  | `1`             |
| `VAL_OBC_Poiseuille`      | OBC Poiseuille 유동 | `1`             |
| `VAL_Periodic_Poiseuille` | Periodic Poiseuille 유동   | `1`             |

각 해석에서 원하는 `grid_number` 값을 입력하면 해당 데이터가 추출됩니다. 또한, 원하는 해석을 추가하여 진행 가능합니다.

---

## 컴파일 방법

Python 코드(`main.py`)를 실행 파일(`main.exe`)로 변환하려면 다음 명령어를 사용합니다.

```sh
pyinstaller -F main.py
```

- `-F` 옵션: 하나의 실행 파일로 생성 (`dist/main.exe` 위치에 파일이 생성됨).
- `main.py`: 실행할 Python 코드 파일.

컴파일이 완료되면 **현재 디렉토리 내의 `dist/` 폴더**에 `main.exe` 파일이 생성됩니다.

---

## 실행 방법

생성된 `main.exe` 실행 파일을 사용하여 시뮬레이션을 실행할 수 있습니다.

```sh
main.exe --json_pth sample.json
```
또는
```sh
main.exe -j sample.json
```

### 실행 옵션 설명

- `--json_pth sample.json`: JSON 설정 파일(`sample.json`)을 입력하여 실행.
- `-j sample.json`: `--json_pth` 옵션의 단축형.

**예제 실행**
```sh
main.exe --json_pth config.json
main.exe -j config.json
```
위 명령어를 실행하면 `config.json`에 지정된 설정을 기반으로 Solver가 실행됩니다.

---

이 설정 파일을 기반으로 SPH 시뮬레이션을 수행할 수 있습니다. 필요에 따라 `settings`를 수정하여 원하는 해석을 추가할 수 있습니다.