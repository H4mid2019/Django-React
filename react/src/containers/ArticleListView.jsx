import React from 'react';
import Article from'../components/Article';
import axios from 'axios';
import CustomForm from '../components/Form'


class ArticleList extends React.Component {
    state = {
        articles: []
    }

    componentDidMount(){
        axios.get('http://127.0.0.1:8000/blog/api/').then(res => {
            this.setState({
                articles: res.data
            });
            
        })
    }
    render(){
        return (
            <React.Fragment>
            <Article data={this.state.articles}/>
            <br/>
            <h2>Create an article</h2>
            <CustomForm requestType='post' articleID={null} btnText="Create"/>
            </React.Fragment>
        )
    }

}

export default ArticleList