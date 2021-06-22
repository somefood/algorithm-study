package chap03;

import java.util.EmptyStackException;
public class ArrayStack<E> {
    private E s[];
    private int top;
    public ArrayStack() {
        s = (E[]) new Object[1];
        top = -1;
    }
    public int size() {return top+1;}
    public boolean isEmpty() {return (top == -1);}
    
    private void resize(int newSize) {
        Object[] t = new Object[newSize];
        for (int i = 0; i < size; i++) t[i] = a[i];
        a = (E[]) t;
    }
    
    public E peek() {
    	if (isEmpty()) throw new EmptyStackException();
    	return s[top];
    }
    
    public void push(E newItem) {
    	if(size() == s.length) {
    		resize(2 * s.length);
    	}
    	s[++top] = newItem;
    }
    
    public E pop() {
    	if (isEmpty()) throw new EmptyStackException();
    	E item = s[top];
    	s[top--] = null;
    	if(size() > 0 && size() == s.lenth/4)
    		resize(s.length/2);
    	return item;
    }
    
    public static void main() {
		ArrayStack<String> stack = new ArrayStack<>();
		stack.peek();
		stack.push("apple");
	}
}