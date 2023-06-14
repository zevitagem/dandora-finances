/* RESET */

@charset "UTF-8";

* {
    margin: 0;
    padding: 0;

    box-sizing: border-box;

    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* GLOBAL */

@import 'reset';

$bg-color: rgb(90, 60, 150);

@mixin Align($isColumn) {
    display: flex;
    align-items: center;
    justify-content: center;
    
    @if $isColumn == true {
        flex-direction: column;
    }
}

body {
    background: $bg-color;

    width: 100vw;
    height: 100vh;

    @include Align(false);
}

/* GAME */

@import 'reset';
@import 'global';

#game {
    background: linear-gradient(
        180deg, 
        rgba(93, 211, 255, 0.5) 0%, 
        rgba(94, 204, 255, 0.5) 33.65%, 
        rgba(94, 192, 255, 0.5) 65.42%, 
        rgba(94, 195, 255, 0.5) 100%
    );
    backdrop-filter: blur(12.5px);

    width: 18em;
    height: 36em;

    border-radius: 1em;
    padding: 1em;

    position: relative;

    @include Align(false);
    @include box-shadow();
}

/* BOARD */

@import 'reset';
@import 'global';
@import 'game';

@mixin box-shadow() {
    box-shadow: .25em .25em .25em .25em rgba(0, 0, 0, .25);
}

.board {
    width: 16em;
    height: 34em;

    @include Align(true);

    .list-players {
        width: 15em;
        height: 7.5em;

        display: flex;
        align-items: center;
        justify-content: space-between;

        img {
            width: 3em;
            height: 3em;

            margin: .25em;
            border-radius: 50%;
        }

        .data {
            @include Align(true);

            .player, .score {
                color: #FFFFFF;
            
                width: 65px;

                margin: .25em;

                font-family: 'Poppins';
                font-style: normal;
                font-weight: 600;
                font-size: 1em;

                line-height: 1.25em;
            }
        }
    }

    hr {
        width: 15em;

        margin: 1em;
        border: 1px solid #FFFFFF;
    }

    .moves {
        width: 15em;
        height: 19em;

        @include Align(true);
        
        .message {
            background: #8FBCFE;
            color: rgba(255, 255, 255, 1);
            
            width: 15em;
            height: 5em;
            
            margin: 1em;
            border-radius: .5em;
            padding: 1em;

            @include Align(false);
            @include box-shadow();

            font-family: 'Poppins';
            font-style: normal;
            font-weight: 700;
            font-size: 1em;

            line-height: 30px;
        }

        .play-block {
            @include Align(false);
            
            .block {
                background: #8FBCFE;
                
                width: 4.5em;
                height: 4.5em;

                margin: .4em;
                border-radius: .5em;
                padding: 1em;

                @include box-shadow();

                cursor: pointer;

                &:hover {
                    background: #3f577a;
                }
            }
        }
    }

    .config {
        width: 15em;
        height: 7.5em;

        @include Align(true);
        
        button {
            background: #E4F0FF;
            
            width: 18em;
            height: 4em;

            margin: .5em;
            border: none;
            border-radius: 10px;

            @include box-shadow();

            cursor: pointer;
            
            &:hover {
                background: rgb(210, 220, 230);
            }
        }

        .title {
            color: #656565;

            font-family: 'Poppins';
            font-style: normal;
            font-weight: 700;
            font-size: 1em;

            line-height: 20px;
        }
    }
}