from __future__ import annotations
from typing import Any, Type


Null = -1


class Node:
    def __init__(self, data = Null, next = Null, dnext = Null):
        self.data = data    # 데이터
        self.next = next    # 리스트의 뒤쪽 포인터
        self.dnext = dnext  # 프리 리스트의 뒤쪽 포인터


class ArrayLinkedList:
    """연결 리스트 클래스(배열 커서 버전)"""

    def __init__(self, capacity: int):
        self.head = Null                    # 머리 노드
        self.current = Null                 # 주목 노드
        self.max = Null                     # 사용 중인 꼬리 레코드
        self.deleted = Null                 # 프리 리스트의 머리 노드
        self.capacity = capacity            # 리스트의 크기
        self.n = [Node() * self.capacity]   # 리스트 본체
        self.no = 0

    def __len__(self) -> int:
        return self.no

    def get_insert_index(self):
        """다음에 삽입할 레코드의 인덱스를 구함"""
        if self.deleted == Null:
            if self.max < self.capacity:
                self.max += 1
                return self.max
            else:
                return Null
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext
            return rec
    
    def delete_index(self, idx: int) -> None:
        if self.deleted == Null:
            self.deleted == idx
            self.n[idx].dnext = Null
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[rec].dnext = rec
    
    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr != Null:
            if self.n[ptr].data == data:
                self.curret = ptr
                return cnt
            cnt += 1
            ptr = self.n[ptr].next
        return Null

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def add_first(self, data: Any):
        ptr = self.head
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec
            self.n[self.head] = Node(data, ptr)
            self.no += 1
    
    def add_last(self, data: Any) -> None:
        if self.head == Null:
            self.add_first(data)
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()

            if rec != Null:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        if self.head != Null:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1
        
    def remove_last(self) -> None:
        if self.head != Null:
            if self.n[self.head].next == Null:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = Null
    
    def remove(self, p: int) -> None:
        if self.head != Null:
            if p == sef.head:
                self.remove_first()
            ese:
            ptr = self.head

            while self.n[ptr].next != p:
                ptr = self.n[ptr].next
                if ptr == Null:
                    return
            self.n[ptr].next = Null
            self.delete_index(ptr)
            self.n[ptr].next = self.n[p].next
            self.current = ptr
            self.no -= 1
        
    def remove_current_node(self) -> None:
        self.remove(self.current)
    
    def clear(self) -> None:
        while self.head != Null:
            self.remove_first()
        self.current = Null
    
    def next(self) -> bool:
        if self.current == Null or self.n[self.current].next == Null:
            return False
        self.current = self.n[self.current].next
        return True
    
    def print_current_node(self) -> None:
        if self.current == Null:
            print('주목 노드가 없습니다.')
        else:
            print(self.n[self.current].data)
    
    def print(self) -> None:
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next
    
    def dump(self) -> None:
        for i in self.n:
            print(f'[{i}] {i.data} {i.next} {i.dnext}')
    
    def __iter__(self) -> ArrayLinkedListIterator:
        return ArrayLinkedListIterator(self.n, self.head)


class ArrayLinkedListIterator:
    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head
    
    def __iter__(self) -> ArrayLinkedListIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data