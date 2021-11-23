# 세이브파일 관련 모듈
import sys
import os
import pickle


#===== 전역정의부 =====#
dir_name = 'C:/Users/pink0/Desktop/승연수업/team_home/team'
file_name1 = 'user_list.sav'
file_name2 = 'book_store.sav'



user_list = [
    {
        "id": "abc123",
        "pw": "1234!",
        "name": "김철수"
    },
    {
        "id": "def123",
        "pw": "5432!",
        "name": "홍길동"
    }
]


book_store = [
    {
        '책번호': 'a001',
        '책이름': '삼국지',
        '가격': 9000,
        '수량': 2,
        '총액': 18000
    },
    {
        '책번호': 'a002',
        '책이름': '해리포터',
        '가격': 8000,
        '수량': 6,
        '총액': 48000
    },
    {
        '책번호': 'a003',
        '책이름': '어린왕자',
        '가격': 7500,
        '수량': 2,
        '총액': 15000
    }
]



#===== 함수 정의부 =====#
####user 리스트
# 세이브 파일 생성 함수
def save_user_list():
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    try:
        # b모드는 딕셔너리나 리스트같은 객체를 통째로 넣을 때 사용하는 모드
        f = open(dir_name+file_name1, 'wb')
        pickle.dump(user_list, f) #리스트를 통째로 세이브파일에 저장
    except:
        print('파일 저장 실패')
    finally:
        f.close()

# 파일 로드 기능 함수
def load_user_list():
    global user_list    

    if not os.path.isdir(dir_name): return
    if not os.path.isfile(dir_name+file_name1): return

    try:
        f = open(dir_name+file_name1, 'rb')
        user_list = pickle.load(f)
    except:
        print('파일 로드 실패')
    finally:
        f.close()

####book 리스트
# 세이브 파일 생성 함수
def save_book_store():
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    try:
        # b모드는 딕셔너리나 리스트같은 객체를 통째로 넣을 때 사용하는 모드
        f = open(dir_name+file_name2, 'wb')
        pickle.dump(book_store, f) #리스트를 통째로 세이브파일에 저장
    except:
        print('파일 저장 실패')
    finally:
        f.close()

# 파일 로드 기능 함수
def load_book_store():
    global book_store    

    if not os.path.isdir(dir_name): return
    if not os.path.isfile(dir_name+file_name2): return

    try:
        f = open(dir_name+file_name2, 'rb')
        book_store = pickle.load(f)
    except:
        print('파일 로드 실패')
    finally:
        f.close()


#첫 회원가입/로그인 화면 보여주기
def show_first():
    print('\n\n=====================================')
    print("=====> 도서 재고관리 프로그램 <=====")
    print('='*37)
    print('1. 신규 직원 등록하기')
    print('2. 기존 직원 로그인하기')
    print('3. 직원 정보 조회하기')
    
    print('4. 프로그램 종료하기')
    print('='*37)

# 회원정보 화면 출력
def show_users_info():
    print('\n\n==============================')
    print('=====> 직원 정보 관리 <=====')
    print('='*30)
    print('1. 직원 정보 수정하기')
    print('2. 직원 정보 삭제하기')
    print('3. 처음 화면으로 돌아가기')
    print('='*30)

#중복을 확인하는 함수(아이디)
def check_duplicate_code_id():
    while True:

        code = input('\n아이디 >> ')
        flag = False  # 중복 플래그

        # 제품번호 중복검증
        for u in user_list:
            if code == u['id']:

                # 중복된 경우
                print('\n!!! 아이디가 이미 존재합니다. 다시 입력하세요 !!!')
                flag = True
                break
        if flag == False:
            return code     # 중복안된 제품번호


# 신규직원등록 (회원가입)
def insert_id_pw():    
    
    user = {}
    print('\n>>> 신규 직원 등록을 시작합니다.')
    print('>>> (영문/숫자/문자로 입력해주세요)')
    user['id'] = check_duplicate_code_id()
    user['pw'] = input('비밀번호 >> ')
    user['name'] = input('이름 >> ')

    user_list.append(user)
    
    print('\n>> 회원가입이 완료되었습니다. <<')
    save_user_list()
    

# 기존 직원 로그인
# 아이디를 입력받는
def input_id():
    return input('\n아이디 >> ') 
# 비번을 입력받는
def input_pw():
    return input('비밀번호 >> ') 



#아이디로 정보를 찾아오는
def find_login(find_id):
    for already_user in user_list:
        if find_id == already_user['id']:
            return already_user
    return {}

'''
#비밀번호로 정보를 찾아오는
def find_login(find_pw):
    for already_user in user_list:
        if find_pw == already_user['pw']:
            return already_user
    return {}
'''

# 로그인 하는
def login():
    find_id = input_id()
    already_user = find_login(find_id)
    
    
    if len(already_user) > 0:            
        in_pw = input_pw() # 방금 입력한 비번
        real_pw = already_user['pw']
                            
        while True:
            if in_pw == real_pw:
                print('\n>> {}님, 로그인에 성공하셨습니다. <<'.format(already_user['id']))
                return True
            else :
                print('\n!!! 비밀번호를 잘못 입력했습니다 !!!')
                # 도서목록
                break

                
                                
    else:
        print('\n!!! 가입되지 않은 정보입니다 !!!')

# 직원 정보 출력 머릿말 부분 함수
def header_user_print():
    print('\n\n=====================================')
    print('\t*** 서점 직원 정보 ***')
    print('=' * 37)
    print('{:^10s}{:^12s}{:^14s}'.format('id','pw','name'))
    print('=' * 37)

# 기존 직원 정보 조회하는 함수
def print_all_users():
    header_user_print()

    for users in user_list:
        print('{:^10s}{:^14s}{:^10s}'.format(users['id'],users['pw'],users['name']))
    
    print('=' * 37)

# 회원코드를 입력받는 함수
def input_user_code(msg):
    print(f'\n# {msg}하실 회원의 id를 입력하세요.')
    code_id = input('>> ')
    return code_id

# 회원코드로 해당 회원정보를 찾아오는 함수
def get_user_info(code_id):
    for info in user_list:
        if code_id == info['id']:
            return info
    return {}

# 회원정보 수정 처리 함수
def modify_info():
    code_id = input_user_code('수정')
    info = get_user_info(code_id)

    if len(info) > 0:
        print('\n# [ID: {}] {}님의 정보를 수정합니다.'.format(info['id'],info['name']))

        print('[ 1. id 변경 | 2. pw 변경 | 3. name 변경 | 4. 취소 ]')
        select = int(input('>> '))

        if select == 1:
            info['id'] = input('\n>> ID 수정(변경 전: {}) >> '.format(info['id']))
            print('\n>> 정보수정이 정상 처리되었습니다. <<')

        elif select == 2:
            info['pw'] = input('\n>> PW 수정(변경 전: {}) >> '.format(info['pw']))
            print('\n>> 정보수정이 정상 처리되었습니다. <<')
        elif select == 3:
            info['name'] = input('\n>> 이름 수정(변경 전: {}) >> '.format(info['name']))
            print('\n>> 정보수정이 정상 처리되었습니다. <<')
        else:
            print('\n# 변경을 취소합니다.')

    else:
        print('\n[ID : {}] 해당하는 직원 정보가 등록되지 않았습니다.'.format(code_id))
    save_user_list()

# 회원정보 삭제 처리 함수
def delete_info():
    code_id = input_user_code('삭제')
    info = get_user_info(code_id)

    if len(info) > 0:
        user_list.remove(info)
        print('\n>> {}님의 정보삭제가 정상 처리되었습니다. <<'.format(info['name']))

    else:
        print('\n[ID: {}]에 해당하는 직원 정보가 등록되지 않았습니다.'.format(code_id))
    save_user_list()


           
######################################################################################
   
# 로그인 이후 나오는 도서 재고관리 프로그램
# 로그인 이후 나오는 메뉴 출력함수
def show_second():
    print("\n\n=========================")
    print('# 1. 신규 도서 등록하기')
    print('# 2. 모든 도서 조회하기')
    print('# 3. 개별 도서 조회하기')
    print('# 4. 도서 정보 수정')
    print('# 5. 도서 정보 삭제')
    print('# 6. 프로그램 종료')
    print("=========================")

# 도서 번호의 중복을 확인하는 함수
def check_book_code():
    while True:
        print('>>> 도서번호 예시: a001, a002, ...')
        book_code = input('\n도서 번호 >> ')

        flag = False

        for b in book_store:
            if book_code == b['책번호']:
                print('\n>>> 도서 번호가 중복되었습니다. 다시 입력하세요.')
                flag = True
                break
        if flag == False:
            return book_code


# 신규 도서 등록 함수
def ipt_book():
    book = {}
    print('\n>>> 도서 정보 등록을 시작합니다.')

    book['책번호'] = check_book_code()
    book['책이름'] = input('도서명 >> ')
    book['가격'] = int(input('가격 >> '))
    book['수량'] = int(input('수량 >> '))
    book['총액'] = book['가격'] * book['수량']

    book_store.append(book)
    print('\n>> 신규 도서가 등록되었습니다. <<')
    save_book_store()
    

# 도서정보 출력 머리말
def books_header():
    print('\n\n\t\t ***** 도서 재고 조회 *****')
    print('=' * 60)
    print('{:<7s}{:^12s}{:^10s}{:^7s}{:^12s}'.format('책번호','책이름','가격','수량','총액'))
    print('=' * 60)
    
# 전체 도서정보를 출력하는 함수
def all_books():
    books_header()

    total_price =0
    for book in book_store:
        total_price += book['총액']
        print('{:<7s}{:^16s}{:>8d}원{:>7d}개{:>12d}원'.format(book['책번호'],book['책이름'],book['가격'],book['수량'],book['총액']))
    print('=' * 60)
    print(f'\t\t도서 재고 총액: {total_price}원')

# 도서번호를 입력받는 함수
def input_code(msg):
    print(f'\n\n>> {msg}하실 제품의 번호를 입력하세요')
    print('>> 도서번호 예시: a001, a002, ...')
    book_code = input('도서번호 >> ')
    return book_code


# 도서번호로 해당 제품을 찾아오는 함수
def search_code(book_code):
    for book in book_store:
        if book_code == book['책번호']:
            return book
    return {}

# 개별 도서 정보 조회
def search_book():
    book_code = input_code('조회')
    book = search_code(book_code)   
    
    if len(book) > 0:
        books_header()
        print('{:<7s}{:^16s}{:>8d}원{:>7d}개{:>12d}원'.format(book['책번호'],book['책이름'],book['가격'],book['수량'],book['총액']))
        print('=' * 60)
    else:
        print('\n!! 존재하지 않는 도서입니다. !!')

# 도서 정보 수정하기
def modify_book():
    book_code = input_code('수정')
    book = search_code(book_code)

    if len(book) > 0:
        print('\n# [{}] {}의 정보를 수정합니다.'.format(book['책번호'],book['책이름']))
        print('[ 1. 수량 변경 | 2. 단가 변경 | 3. 일괄 변경 | 4. 취소 ]')
        select = int(input('=> '))
        if select == 1:         
            book['수량'] = int(input('=> 수정할 수량({}) >> '.format(book['수량'])))
            print('\n>> 정보수정이 정상 처리되었습니다. <<')
        elif select == 2:
            book['가격'] = int(input('=> 수정할 가격({}) >> '.format(book['가격'])))
            print('\n>> 정보수정이 정상 처리되었습니다. <<')
        elif select == 3:
            book['수량'] = int(input('=> 수정할 수량({}) >> '.format(book['수량'])))
            book['가격'] = int(input('=> 수정할 가격({}) >> '.format(book['가격'])))
            print('\n>> 정보수정이 정상 처리되었습니다. <<')
        else:
            print('# 변경을 취소합니다.')
        book['총액'] = book['가격'] * book['수량']
    else:
        print('\n!! 존재하지 않는 도서입니다. !!')
    save_book_store()
    

# 도서정보 삭제 처리 함수
def delete_book():
    book_code = input_code('삭제')
    book = search_code(book_code)

    if len(book) > 0:
        book_store.remove(book)
        print('\n>> 도서가 정상 삭제되었습니다. <<')
    else:
        print('\n!! 존재하지 않는 도서입니다. !!')
    save_book_store()
    
        

##################################################################################

#프로그램 종료처리하기
def exit_program():
    import sys
    print('\n>> 프로그램을 종료합니다. [Y/N]')
    answer = input('>> ')
    if answer.lower()[0] == 'y':
        sys.exit()
    else:
        return

############################################################################

#실행부
if __name__ == '__main__':
    load_user_list()

    while True:
        show_first()
        
        menu = int(input('\n>>> '))
        
        if menu == 1:
            insert_id_pw()
        elif menu == 2:
            
            is_login = login()


            if is_login:
                load_book_store()
                # is_login이 True => 도서 등록 메뉴로 전환
                while True:
                    show_second()
                    book_info = int(input('\n>>> '))

                    if book_info == 1:
                        ipt_book()
                    elif book_info == 2:
                        all_books()
                    elif book_info == 3:
                        search_book()
                    elif book_info == 4:
                        modify_book()
                    elif book_info == 5:
                        delete_book()
                    elif book_info == 6:
                        exit_program()
                    else:
                        print('!! 메뉴를 잘못 입력했습니다. !!')

                    input('\n>> 메뉴화면으로 돌아가시려면 Enter를 누르세요.')

        elif menu == 3:
            

            is_all_users_info = print_all_users()

            while True:
                    show_users_info()
                    trans_info = int(input('\n>>> '))
                    
                    if trans_info == 1:
                        modify_info()
                    elif trans_info == 2:
                        delete_info()
                    elif trans_info == 3:
                        break
                    else:
                        print('!! 메뉴를 잘못 입력했습니다. !!')

            '''
            if is_all_users_info:
                load_user_list()

                while True:
                    show_users_info()
                    trans_info = int(input('\n>>> '))
                    
                    if trans_info == 1:
                        modify_info()
                    elif trans_info == 2:
                        delete_info()
                    elif trans_info == 3:
                        exit_program
                    else:
                        print('!! 메뉴를 잘못 입력했습니다. !!')
                    input('\n>> 메뉴화면으로 돌아가시려면 Enter를 누르세요.')
            '''

        elif menu == 4:
            exit_program()
        
        
        else:
            print('!! 메뉴를 잘못 입력했습니다. !!')

        input('\n>> 메뉴화면으로 돌아가시려면 Enter를 누르세요.')
        
            

    
