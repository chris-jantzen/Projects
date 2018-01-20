/*
        Final Project CS1
        Connect 4
        Robert Bolgzds
        Chris Jantzen
        Chris Messmer
        
        
        **NOTE: When compiling, use g++ -std=c++11 connect4.cpp
*/

#include <iostream>
#include <array>
#include <vector>
#include <ios>
#include <limits>
#include <string>
#include <time.h>
#include <cctype>

using namespace std;

class connectFour{
private:
    char p1;
    char p2;
    char grid[6][7];
    

public:
    bool fourInRow(char p){
        int count;
        for(unsigned r = 0; r < 6; r++){
            for(unsigned c = 0; c < 7; c++){
                if(r == 0){
                    if(c == 0){
                        count = rowRight( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = diagDownRight( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = colDown( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                    }else if(c == 6){
                        count = rowLeft( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = diagDownLeft( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = colDown( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                    }else{
                        count = rowLeft( r, c, p) + rowRight( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = colDown( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = diagDownLeft( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = diagDownRight( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                    }
                }else if(r == 5){
                    if(c == 0){
                        count = rowRight( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = diagUpRight( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = colUp( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                    }else if(c == 6){
                        count = rowLeft( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = diagUpLeft( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = colUp( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                    }else{
                        count = rowLeft( r, c, p) + rowRight( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = colUp( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = diagUpLeft( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                        count = diagUpRight( r, c, p) + 1;
                        if(win(count)){
                            return true;
                        }
                    }
                }else{
                    count = rowLeft( r, c, p) + rowRight( r, c, p) + 1;
                    if(win(count)){
                        return true;
                    }
                    count = colUp( r, c, p) + colDown( r, c, p) + 1;
                    if(win(count)){
                        return true;
                    }
                    count = diagDownLeft( r, c, p) + diagUpRight( r, c, p) + 1;
                    if(win(count)){
                        return true;
                    }
                    count = diagUpLeft( r, c, p) + diagDownRight( r, c, p) + 1;
                    if(win(count)){
                        return true;
                    }
                }
            }
        }
        return false;
    }

    int diagUpLeft(int rpos, int cpos, char p){
        int count = 0;
        if(grid[rpos][cpos] != p){
        	return count;
        }
        rpos--;
        cpos--;
        while(grid[rpos][cpos] == p){
            if(rpos < 0 || cpos < 0){
                return count;
            }
            count++;
            rpos--;
            cpos--;
        }
        return count;
    }

    int diagDownLeft(int rpos, int cpos, char p){
        int count = 0;
        if(grid[rpos][cpos] != p){
        	return count;
        }
        rpos++;
        cpos--;
        while(grid[rpos][cpos] == p){
            if(rpos > 5 || cpos < 0){
                return count;
            }
            count++;
            rpos++;
            cpos--;
        }
        return count;
    }

    int diagUpRight(int rpos, int cpos, char p){
        int count = 0;
        if(grid[rpos][cpos] != p){
        	return count;
        }
        rpos--;
        cpos++;
        while(grid[rpos][cpos] == p){
            if(rpos < 0 || cpos > 6){
                return count;
            }
            count++;
            rpos--;
            cpos++;
        }
        return count;
    }

    int diagDownRight(int rpos, int cpos, char p){
        int count = 0;
        if(grid[rpos][cpos] != p){
        	return count;
        }
        rpos++;
        cpos++;
        while(grid[rpos][cpos] == p){
            if(rpos > 5 || cpos > 6){
                return count;
            }
            count++;
            rpos++;
            cpos++;
        }
        return count;
    }

    int rowRight(int rpos, int cpos, char p){
        int count = 0;
        if(grid[rpos][cpos] != p){
        	return count;
        }
        cpos++;
        while(grid[rpos][cpos] == p){
            if(cpos > 6){
                return count;
            }
            count++;
            cpos++;
        }
        return count;
    }

    int rowLeft(int rpos, int cpos, char p){
        int count = 0;
        if(grid[rpos][cpos] != p){
        	return count;
        }
        cpos--;
        while(grid[rpos][cpos] == p){
            if(cpos < 0){
                return count;
            }
            count++;
            cpos--;
        }
        return count;
    }

    int colUp(int rpos, int cpos, char p){
        int count = 0;
        if(grid[rpos][cpos] != p){
        	return count;
        }
        rpos--;
        while(grid[rpos][cpos] == p){
            if(rpos < 0){
                return count;
            }
            count++;
            rpos--;
        }
        return count;
    }

    int colDown(int rpos, int cpos, char p){
        int count = 0;
        if(grid[rpos][cpos] != p){
        	return count;
        }
        rpos++;
        while(grid[rpos][cpos] == p){
            if(rpos > 5){
                return count;
            }
            count++;
            rpos++;
        }
        return count;
    }

    bool win(int count){
        if(count >= 4){
            return true;
        }else{
            return false;
        }
    }

    connectFour(char p1_in,char p2_in){
        setp1(p1_in);
        setp2(p2_in);
        char grid_in[6][7] = { {'_','_','_','_','_','_','_'},
                               {'_','_','_','_','_','_','_'},
                               {'_','_','_','_','_','_','_'},
                               {'_','_','_','_','_','_','_'},
                               {'_','_','_','_','_','_','_'},
                               {'_','_','_','_','_','_','_'} };

        setgrid(grid_in);
        boardshape();
    }
    connectFour (char p1_in){
        char p2_in = p1_in-1;
        setp1(p1_in);
        setp2(p2_in);
        char grid_in[6][7] = { {'_','_','_','_','_','_','_'},
                               {'_','_','_','_','_','_','_'},
                               {'_','_','_','_','_','_','_'},
                               {'_','_','_','_','_','_','_'},
                               {'_','_','_','_','_','_','_'},
                               {'_','_','_','_','_','_','_'} };
        setgrid(grid_in);
        boardshape();

    }
    char getP2(){
        return p2;
    }
    void turn(int column,char p){
        int row =6;
        column--;
        while(column<0||column>6){

            if(cin.fail()){
                while(cin.fail()){
                    cin.clear();
                    cin.ignore(10, '\n');
                    cout<<"That's not even a number. Try again:"<<endl;
                    cin>>column;
                }
            }
            else{
                cout<<"Invalid entry, try again:"<<endl;
                cin>>column;
            }
            column--;
        }
        turn(column,row,p);
        fourInRow(p);
    }
    void turn(int column, int row,char p){
        if(grid[row][column] == '_'){
            grid[row][column] =  p;
            return;
        }
        else if(row == 0){
            cout<< "Column full."<<endl;
            turn(10,p);
        }
        row--;
        turn(column,row,p);
    }

    void boardshape(){
        for(int r=0;r<6;r++){
            cout<<"|";
            for(int c=0;c<7;c++){
                cout<<grid[r][c]<<"|";
            }
            cout<<endl;
        }
        cout << " -+-+-+-+-+-+- " << endl;
        cout << " 1 2 3 4 5 6 7 " << endl;
    }

    void setp1(char p1_in){

        p1 = p1_in;
    }
    void setp2(char p2_in){

        p2 = p2_in;
    }
    void setgrid(char grid_in[6][7]){
        for(int r=0;r<6;r++){
            for(int c=0;c<7;c++){
                grid[r][c] = grid_in[r][c];
            }
        }
    }
    char getp1(){
        return p1;
    }
    char getp2(){
        return p2;
    }
    
    void cpuTurn(){
        aiColMove(p2);
    }
    int randCol(){
        srand(time(0));
        return rand()%7+1;
    }
    int aiColMove(char cOpp){
        //returns column number to drop in
        int iColMove = randCol()-1, iScoreMax = 0;
        int iCount;
        for(int iCol = 0; iCol < 7; iCol++){
            int iScore = 0;
            int iRow = rowOnDrop(iCol);
            if(iRow == -1) continue;
            //if ai can win, it will, otherwise it will make a defensive move
            //Horizontal
            if(scoreDir(iRow,iCol,0,1,p2) >= 9) return iCol+1;
            iScore = max(iScore, scoreDir(iRow,iCol,0,1,cOpp));
            //Diagonal Up Right
            if(scoreDir(iRow,iCol,-1,1,p2) >= 9) return iCol+1;
            iScore = max(iScore, scoreDir(iRow,iCol,-1,1,cOpp));
            //Diagonal Up Left
            if(scoreDir(iRow,iCol,-1,-1,p2) >= 9) return iCol+1;
            iScore = max(iScore, scoreDir(iRow,iCol,-1,-1,cOpp));
            //Vertical
            if(countDir(iRow,iCol,1,0,p2) == 3) return iCol+1;
            iCount = countDir(iRow,iCol,1,0,cOpp);
            if(iCount > 2){
                iScore = max(iScore,10);
            }
            else if(iCount == 2){
                iScore = max(iScore,3);
            }
            else if(iCount == 1){
                iScore = max(iScore,2);
            }
            //Check for new high score
            if(iScore > iScoreMax){
                iScoreMax = iScore;
                iColMove = iCol;
            }
        }
        cout << iColMove+1 << endl;
        return iColMove+1;
    }
    
    int max(int i1, int i2){
        if(i1 > i2) return i1;
        return i2;
    }
    
    int rowOnDrop(int iCol){
        int iRow = -1;
        while(grid[iRow+1][iCol] == '_'){
            if(iRow == 6) return 6;
            iRow++;
        }
        return iRow;
    }
    
    int scoreDir(int iRow, int iCol, int iRowinc, int iColinc, char cOpp){
        int iCount1 = countDir(iRow,iCol,iRowinc,iColinc,cOpp);
        int iCount2 = countDir(iRow,iCol,-iRowinc,-iColinc,cOpp);
        // _xxx xxx_
        if(iCount1 > 2 || iCount2 > 2){
            return 10;
        }
        // xx_x xx_x
        if((iCount1 == 2 && iCount2 == 1) || (iCount1 == 1 && iCount2 == 2)){
            return 9;
        }
        // x_x
        if(iCount1 == 1 && iCount2 == 1){
            return 5;
        }
        // _xx_
        if(iCount1 == 2 || iCount2 == 2){
            return 3;
        }
        // x_
        if(iCount1 == 1 || iCount2 == 1){
            return 2;
        }
        // _
        return 0;
    }
    
    int countDir(int iRow, int iCol, int iRowinc, int iColinc, char cOpp){
        int iScore = 0;
        while(true){
            iRow += iRowinc;
            iCol += iColinc;
            if(iRow > 6 || iRow < 0){
                return iScore;
            }
            if(iCol > 5 || iCol < 0){
                return iScore;
            }
            if(grid[iRow][iCol] == cOpp){
                iScore++;
            }
            else{
                return iScore;
            }
        }
    }
    
    bool fullCheck(){
        for(unsigned r = 0; r < 6; r++){
            for(unsigned c = 0; c < 7; c++){
            	if(grid[r][c] == '_'){
            		return false;
            	}
            }
        }
    	return true;
    }
};



int main(){
    bool p1win = false;
    bool p2win = false;
    bool full = false;
    int players=0,column;
    char temp[2];
    char p1_in,p2_in;

    cout<<"How many players?"<<endl<<"1 : Enter 1"<<endl<<"2 : Enter 2"<<endl;


    do{
        cin>>players;
        if(players == 1){
            int k = 0;
            string input;
            
            while(input[0] == '_'||input.length()!=1){
                if(k>0){
                    cout<<"Player 1 enter a single character"<<endl;
                }
                k++;
                input.clear();
                getline(cin,input);
            }
            p1_in = input[0];
            connectFour oneplayer(p1_in);

            while((p1win == false && p2win == false) && full == false){
                cout << "Player 1, choose a column (1-7)." << endl;
                cin >> column;
                oneplayer.turn(column,p1_in);
                oneplayer.boardshape();
                p1win = oneplayer.fourInRow(p1_in);
                if(p1win){
                    cout<<"Player 1 wins!"<<endl;
                    break;
                }
                full = oneplayer.fullCheck();
                if(full){
                	cout << "Board full, try again!" << endl;
                	break;
                }
                
                oneplayer.turn(oneplayer.aiColMove(p1_in),oneplayer.getp2());
                oneplayer.boardshape();
                p2win = oneplayer.fourInRow(oneplayer.getp2());
                if(p2win){
                    cout<<"CPU wins!"<<endl;
                    break;
                }
                full = oneplayer.fullCheck();
                if(full){
                	cout << "Board full, try again!" << endl;
                	break;
                }
            }
        }
        
        
        else if(players == 2){
            int k = 0;
            string input;
            while(input[0] == '_'||input.length()!=1){
                if(k>0){
                    cout<<"Player 1 enter a single character"<<endl;
                }
                k++;
                input.clear();
                getline(cin,input);
            }
            p1_in = input[0];
            input.clear();
            
            while(input[0] == '_'||input.length()!=1){
                input.clear();
                cout<<"Player 2 enter a single character"<<endl;
                getline(cin,input);
            }
            p2_in = input[0];
            connectFour twoplayer(p1_in,p2_in);

            while((p1win == false && p2win == false) && full == false){
                cout<<"Player 1, choose a column (1-7)."<<endl;
                cin>>column;
                twoplayer.turn(column,p1_in);
                twoplayer.boardshape();
                p1win = twoplayer.fourInRow(p1_in);
                if(p1win){
                    cout<<"Player 1 wins!"<<endl;
                    break;
                }
                full = twoplayer.fullCheck();
                if(full){
                	cout << "Board full, try again!" << endl;
                	break;
                }
                
                cout<<"Player 2, choose a column (1-7)."<<endl;
                cin>>column;
                twoplayer.turn(column,p2_in);
                twoplayer.boardshape();
                p2win = twoplayer.fourInRow(p2_in);
                if(p2win){
                    cout<<"Player 2 wins!"<<endl;
                    break;
                }
                full = twoplayer.fullCheck();
                if(full){
                	cout << "Board full, try again!" << endl;
                	break;
                }
            }
        }
        else{
            cin.clear();
            cin.ignore(10, '\n');
            cout<<"Invald amount of players, Try again:"<<endl;
        }
    }while(players!=1&&players!=2);

}
