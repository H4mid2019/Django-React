import React from 'react';
import axios from 'axios';
import { Card, Button } from 'antd';
import CustomForm from '../components/Form'


class ArticleDetail extends React.Component {
    state = {
        article: {}
    }

    componentDidMount(){
        const articleID = this.props.match.params.articleID
        axios.get(`http://127.0.0.1:8000/blog/api/${articleID}`).then(res => {
            this.setState({
                article: res.data
            });
            console.log(res.data)
        })
    }
    handleDel=(event)=>{
        const articleID = this.props.match.params.articleID
        axios.delete(`http://127.0.0.1:8000/blog/api/${articleID}`);
        this.props.history.push('/');
        this.forceUpdate();
    }
    render(){
        return (
            <React.Fragment>
            <Card title={this.state.article.title}>
                <p>{this.state.article.brief}</p>
                <br/>
                <div>
                {this.state.article.article}
                </div>
            </Card>
            <CustomForm requestType='put' articleID={this.props.match.params.articleID} btnText="Update"/>
            <form onSubmit={this.handleDel}>
            <Button type="danger" htmlType="submit">Delete</Button>
            </form>
            </React.Fragment>
        )
    }

}

export default ArticleDetail