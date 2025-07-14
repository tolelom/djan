# saju/views.py
from django.shortcuts import render, redirect

def input_view(request):
    # GET: 입력 폼 표시
    return render(request, 'saju/input.html')

def result_view(request):
    # POST: 폼 처리 후 결과 페이지로 렌더링
    if request.method == 'POST':
        name        = request.POST.get('name')
        birth_date  = request.POST.get('birthDate')
        birth_time  = request.POST.get('birthTime')
        birth_place = request.POST.get('birthPlace')

        if not all([name, birth_date, birth_time, birth_place]):
            msg = "모든 정보를 입력해주세요."
            return render(request, 'saju/input.html', {'error': msg})

        context = {
            'name': name,
            'birth_date': birth_date,
            'birth_time': birth_time,
            'birth_place': birth_place,
            'main_charts': [
                {'id':'D1','title':'D1 - 라시 차트','description':'기본 출생 차트'},
                {'id':'D9','title':'D9 - 나밤사 차트','description':'결혼과 배우자'},
                {'id':'D10','title':'D10 - 다상사 차트','description':'직업과 경력'},
            ],
            'aux_charts': [
                {'id':'D2','title':'D2 - 호라','description':'재산과 부'},
                {'id':'D3','title':'D3 - 드레카나','description':'형제자매'},
                {'id':'D7','title':'D7 - 삽탐사','description':'자녀와 후손'},
                {'id':'D12','title':'D12 - 드와다사','description':'부모와 조상'},
            ],
            'today_info': {
                'time': '현재 다샤 시간',
                'description': '금성 마하디샤 + 목성 안타르다샤',
                'advice': '예술적 노력과 의미 있는 관계 구축에 집중하세요.',
            },
        }
        return render(request, 'saju/result.html', context)
    return redirect('saju:input')
