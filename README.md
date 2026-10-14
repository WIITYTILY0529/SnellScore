# SnellScore

볼넷 성향과 존 판단 관련 지표를 20–80 스케일로 변환해 타자와 투수의 Snell Score를 계산하는 연구 프로젝트입니다.

## 지표

- 타자: 낮은 볼넷 비율과 낮은 존 밖 스윙 비율을 결합합니다.
- 투수: 높은 볼넷 비율과 낮은 meatball 비율을 결합합니다.
- 각 구성 요소는 모집단 평균 50, 표준편차 10인 20–80 스케일로 변환합니다.

현재 정의는 기존 코드의 계산 방식을 정리한 것이며, 지표의 야구적 해석과 필터 기준은 추가 검증이 필요합니다.

## 구조

```text
data/raw/          원본 입력 CSV
src/snell_score/   재사용 가능한 계산 로직
scripts/           분석 실행 진입점
outputs/tables/    생성된 점수표
tests/             핵심 계산 테스트
archive/           구조 개편 전 실험 코드와 의존성 파일
```

원본 데이터는 삭제하거나 수정하지 않습니다.

## 설치

```powershell
python -m pip install -e ".[dev]"
```

## 실행

프로젝트 루트에서 실행합니다.

```powershell
python scripts/run_hitter_analysis.py
python scripts/run_pitcher_analysis.py
```

출력은 각각 다음 위치에 저장됩니다.

- `outputs/tables/snellscorehitter.csv`
- `outputs/tables/snellscorepitcher.csv`

## 테스트

```powershell
pytest
```

## Windows 가상환경

이 폴더 전용 Python 3.12 `.venv`와 의존성을 구성했습니다. PowerShell에서 사용합니다.

```powershell
Set-Location '<BASEBALL_ROOT>\01_Research\09_SnellScore'
. .\.venv\Scripts\Activate.ps1
python -m pip check
```

활성화 없이 `.\.venv\Scripts\python.exe`로 실행할 수도 있습니다.
VS Code에서는 이 프로젝트 폴더를 열고 `.venv` 인터프리터/노트북 커널을 선택합니다.
`requirements-windows.txt`는 Windows 의존성, `requirements-windows.lock.txt`는 실제 설치 버전입니다.
환경 재생성은 이 프로젝트 폴더에서 실행합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-windows.txt
```

경로를 수정했지만 다음 입력은 현재 없습니다. 원본을 아래 위치에 준비해야 관련 실험이 실행됩니다.

- `data/raw/bb%.csv`

새 환경의 로컬 모듈 경로 등록은 [공통 환경 설정](../../README.md#프로젝트별-환경-설정)을 따릅니다.
